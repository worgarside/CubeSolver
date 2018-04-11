"""
A lot of the code in this file is similar to 'multiphase/table_generator.py', and some is duplicated.
To avoid repeated code and inefficiencies, it would make sens to move the code into a commonly accessible file.
However, the files have been kept separate because there are some intricate changes between the files which
may cause confusion, and also to allow for further changes if necessary
"""

import gc
import json
import os
import time
from multiprocessing import Pool, cpu_count
from sqlite3 import IntegrityError, OperationalError

from cube.cube_class import Cube, Move
from cube.moves import dyn_move

# The target position for this lookup (and inherently the root of the generation)
TARGET_POS = 'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'

# Moves used in this lookup
MOVES = [Move.U2, Move.D2, Move.L2, Move.R2, Move.F2, Move.B2]


def generate_lookup_table(db):
    """
    Creates a large table of positions (depth, position, move_sequence) for adding to the database
    by using the moves defined in the constant
    :param db: Cursor object for executing insertion queries
    """
    print('\n- - Generating half_turn Table... - -')

    db.query('''CREATE TABLE IF NOT EXISTS half_turn (depth INTEGER NOT NULL, position TEXT PRIMARY KEY,
             move_sequence BLOB NOT NULL)''')

    print('  Getting previous depth... ', end='')
    try:
        # Gets previous depth from DB, defaults to 0 for complete regeneration
        depth = db.query('SELECT MAX(depth) FROM half_turn').fetchone()[0]
        if depth is None:
            depth = 0
    except TypeError:
        depth = 0

    print(depth)

    try:
        # Inserts target position into the DB, passes if it's already there
        db.query('INSERT INTO half_turn VALUES (?, ?, ?)', (depth, TARGET_POS, json.dumps([])))
    except IntegrityError:
        pass

    """
    Inserted is a boolean flag to see if the generator function has actually inserted any new data into the database.
    If it has not, then there is no point trying to generate the next level and ergo the table is complete
    """
    inserted = True
    while inserted:
        gc.collect()
        try:
            inserted, depth = generate_next_depth(db, depth)
        except AssertionError as err:
            print(err)


def generate_next_depth(db, depth):
    """
    Generates the next depth level of positions in the database table by iterating through the previous depth
    :param db: Database Cursor object
    :param depth: the current depth level which has already been generated
    :return: boolean flag to state if any data has been inserted; the new max depth value
    """

    # Set of all positions for duplication checking. Uses more memory but greatly optimises processing time
    position_set = gen_position_set(db, depth)
    start_time = int(round(time.time() * 1000))
    depth += 1
    print('%2i' % depth, end='.')

    """
    Create an iterable to be processed by the Pool. It is structured like this:
    [(position String, move_sequence List), position_set]
    """
    iterable = map(lambda e: (e, position_set),
                   db.query('SELECT position, move_sequence FROM half_turn where depth = %i' % (depth - 1)).fetchall())
    print('.', end='')

    # Create a MP Pool and give it the iterable to process across all CPU cores for most efficient processing
    p = Pool(processes=cpu_count())
    pool_result = p.starmap(generate_pos_children, iterable)
    p.close()

    gc.collect()  # Reduce redundant memory usage
    print('.', end='')
    insert_count = 0
    duplication_count = 0
    # Pool returns one list per process (effectively 2D array), which must be iterated through and added to DB
    for result_list in pool_result:
        result_list_length = len(result_list)
        for r in range(result_list_length):
            try:
                # Pop results to reduce memory and try to insert into DB
                result = result_list.pop()
                db.query('INSERT INTO half_turn VALUES (?, ?, ?)',
                         (depth, result[0], json.dumps(result[1])))
                insert_count += 1
            except IntegrityError:
                """
                Some duplications might still occur between moves, but these are still counted as 'insertions'
                to ensure complete generation 
                """
                duplication_count += 1

    db.commit()
    gc.collect()

    # Lots of print statements for analysis of processing and manual estimations of remaining time
    print('.', end='   ')
    end_time = int(round(time.time() * 1000))
    total = (end_time - start_time) / 1000
    print('Time: %10.3fs' % total, end='  |  ')
    print('DB Size: %7.2fMB' % (os.path.getsize('Codebase/database/db.sqlite') / 1000000), end='  |  ')
    print('Rows Added: %10i' % insert_count, end='  |  ')
    print('Duplications: %8i' % duplication_count)
    # need to include duplication count in case of resume with full depth
    return (insert_count + duplication_count > 0), depth


def gen_position_set(db, depth):
    """
    Take all of the positions in the Database and put them into one set for quick duplication checking to reduce
    memory usage
    :param db: Database cursor object
    :param depth: Current depth
    :return: Set of position strings
    """
    position_set = set()

    try:
        result = db.query('SELECT position FROM half_turn WHERE depth <= %i' % depth).fetchall()
        for r in result:
            position_set.add(r[0])
    except OperationalError:
        # OperationalError if the table doesn't exist (or other SQLite errors)
        pass

    return position_set


def generate_pos_children(pos_tuple, position_set):
    """
    Generate the children of a position by using the moves defined in the constant MOVES
    :param pos_tuple: tuple of position data: (position String, move_sequence List)
    :param position_set: the large set must be passed in because the processes do not share memory
    :return: The list of new position data: [(position String, new move_sequence Serialized), (... ]
    """
    result_list = []
    for move in MOVES:
        cube = Cube(pos_tuple[0], True)
        dyn_move(cube, move)

        if cube.position not in position_set:
            result_list.append((cube.position, json.loads(pos_tuple[1]) + [move.value]))

    return result_list
