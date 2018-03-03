import json
import os
import time
from multiprocessing import Pool, cpu_count
from sqlite3 import IntegrityError

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
    db.query('DROP TABLE IF EXISTS %s' % TABLES[phase])

    db.query('''CREATE TABLE IF NOT EXISTS %s (
                    depth INTEGER NOT NULL,
                    position TEXT PRIMARY KEY,
                    move_sequence BLOB NOT NULL)
                ''' % TABLES[phase])

    print('\n  - Generating Table %s... -' % TABLES[phase])
    position_dict = {}  # depth: set(position)
    depth = 0
    position_dict[depth] = [(depth, TARGET_POS, [Move.NONE])]
    db.query('INSERT INTO %s VALUES (?, ?, ?)' % TABLES[phase], (depth, TARGET_POS[phase], json.dumps([])))

    p = Pool(processes=cpu_count())
    inserted = True

    while inserted:
        start_time = int(round(time.time() * 1000))
        inserted = False
        depth += 1
        print('%2i' % depth, end='.')
        pos_list = db.query('SELECT position, move_sequence FROM %s where depth = %i' %
                            (TABLES[phase], depth - 1)).fetchall()

        iterable = map(lambda e: (e, phase), pos_list)
        pool_result = p.starmap(gen_next_level, iterable)
        print('.', end='')

        for result in pool_result:
            for r in result:
                try:
                    db.query('INSERT INTO %s VALUES (?, ?, ?)' % TABLES[phase], (depth, r[0], json.dumps(r[1])))
                    inserted = True
                except IntegrityError:
                    pass

        db.commit()
        print('.', end='   ')

        end_time = int(round(time.time() * 1000))
        total = (end_time - start_time) / 1000
        print('Time: %10.3fs' % total, end='   |   ')
        print('DB Size: %7.2fMB' % (os.path.getsize('PC/data/db.sqlite') / 1000000), end='   |   ')
        print('Rows Added: %i' % (
        db.query('select count(*) from %s WHERE depth = %i' % (TABLES[phase], depth)).fetchone()[0]))
    p.close()


def gen_next_level(pos_tuple, phase):
    result_list = []
    for m in MOVE_GROUPS[phase]:
        c = Cube(pos_tuple[0], True)
        dyn_move(c, m)
        result_list.append((c.position, json.loads(pos_tuple[1]) + [m.value]))

    return result_list
