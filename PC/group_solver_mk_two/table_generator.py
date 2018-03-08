import gc
import json
import os
import time
from multiprocessing import Pool, cpu_count
from sqlite3 import IntegrityError, OperationalError

from cube.cube_class import Cube
from cube.move_class import Move
from cube.moves import dyn_move

TABLES = ['gs2p1', 'gs2p2', 'gs2p3', 'gs2p4']

TARGET_POS = [
    'NDNDNDNDNNNNNNNNNNNNNNNNDNDNNNDNDNNNNNNNNNNNNNDNDNDNDN',
    'DDDDDDDDDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDDDDDDDD',
    'DDDDDDDDDWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNN',
    'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'
]

MOVE_GROUPS = [
    [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.NOT_F, Move.NOT_B],
    [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.F2, Move.B2],
    [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2],
    [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2]
]


def generate_lookup_table(db, phase):
    db.query('''CREATE TABLE IF NOT EXISTS %s (depth INTEGER NOT NULL, position TEXT PRIMARY KEY,
             move_sequence BLOB NOT NULL)''' % TABLES[phase])

    try:
        depth = db.query('SELECT MAX(depth) from %s' % TABLES[phase]).fetchone()[0] - 1
    except TypeError:
        depth = 0

    print('\n  - Generating Table %s... -' % TABLES[phase])
    try:
        db.query('INSERT INTO %s VALUES (?, ?, ?)' % TABLES[phase], (depth, TARGET_POS[phase], json.dumps([])))
    except IntegrityError:
        pass

    inserted = True

    while inserted:
        inserted, depth = generate_next_depth(db, depth, phase)


def generate_next_depth(db, depth, phase):
    position_set = gen_position_set(db, depth, phase)
    start_time = int(round(time.time() * 1000))
    depth += 1
    print('%2i' % depth, end='.')

    iterable = map(lambda e: (e, phase, position_set),
                   db.query('SELECT position, move_sequence FROM %s where depth = %i' % (
                   TABLES[phase], depth - 1)).fetchall())

    p = Pool(processes=cpu_count())
    pool_result = p.starmap(generate_pos_children, iterable)
    p.close()
    print('.', end='')
    insert_count = 0
    duplication_count = 0
    for result_list in pool_result:
        result_list_length = len(result_list)
        for r in range(result_list_length):
            try:
                result = result_list.pop()
                db.query('INSERT INTO %s VALUES (?, ?, ?)' % TABLES[phase],
                         (depth, result[0], json.dumps(result[1])))
                insert_count += 1
            except IntegrityError:
                duplication_count += 1

    db.commit()
    gc.collect()
    print('.', end='   ')
    end_time = int(round(time.time() * 1000))
    total = (end_time - start_time) / 1000
    print('Time: %10.3fs' % total, end='  |  ')
    print('DB Size: %7.2fMB' % (os.path.getsize('PC/data/db.sqlite') / 1000000), end='  |  ')
    print('Rows Added: %10i' % insert_count, end='  |  ')
    print('Duplications: %8i' % duplication_count)
    # need to include duplication account in case of resume with full depth
    return (insert_count + duplication_count > 0), depth


def gen_position_set(db, depth, phase):
    position_set = set()

    try:
        """
        WHERE depth <= depth is to ensure that if the db gen is being resumed, it will only create 
        a pos_set from previous depths to allow furhter generation if this depth is complete 
        (and therefore in the set) but the next may not be complete
        """
        result = db.query('SELECT position FROM %s WHERE depth <= %i' % (TABLES[phase], depth)).fetchall()
        for r in result:
            position_set.add(r[0])
    except OperationalError:
        pass

    return position_set


def generate_pos_children(pos_tuple, phase, position_set):
    result_list = []
    for m in MOVE_GROUPS[phase]:
        c = Cube(pos_tuple[0], True)
        dyn_move(c, m)

        if c.position not in position_set:
            result_list.append((c.position, json.loads(pos_tuple[1]) + [m.value]))

    return result_list
