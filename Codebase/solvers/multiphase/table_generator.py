"""
A lot of the code in this file is similar to 'half_turn/table_generator.py', and some is duplicated.
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

# Each phase has a different target position
TARGET_POS = [
    'NDNDNDNDNNNNNNNNNNNNNNNNDNDNNNDNDNNNNNNNNNNNNNDNDNDNDN',
    'DDDDDDDDDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNDDDDDDDDD',
    'DDDDDDDDDWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNNNNNNNN',
    'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'
]

# Different movesets are used for generating the group in each phase
MOVE_GROUPS_MASTER = [
    [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.NOT_F, Move.NOT_B],
    [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.F2, Move.B2],
    [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2],
    [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2],
]
move_groups = [
    [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.NOT_F, Move.NOT_B],
    [Move.NOT_U, Move.NOT_D, Move.NOT_L, Move.NOT_R, Move.F2, Move.B2],
    [Move.NOT_U, Move.NOT_D, Move.L2, Move.R2, Move.F2, Move.B2],
    []
]


def generate_lookup_table(db, phase, verbose):
    """
    Method to generate a new table in the database for the current phase
    :param db: Database Cursor object
    :param phase: the current phase number
    :param verbose: Changes verbosity of output
    """

    print('\n- - Generating Table multiphase_%i... - -' % phase) if verbose else 0
    db.query('''CREATE TABLE IF NOT EXISTS multiphase_%i (depth INTEGER NOT NULL, position TEXT PRIMARY KEY,
             move_sequence BLOB NOT NULL)''' % phase)

    print('  Getting previous depth... ', end='') if verbose else 0
    try:
        # Gets previous depth from DB, defaults to 0 for complete regeneration
        depth = db.query('SELECT MAX(depth) from multiphase_%i' % phase).fetchone()[0]  # - 1
        if depth is None:
            depth = 0
    except TypeError:
        depth = 0

    print(depth) if verbose else 0

    try:
        # Inserts target position into the DB, passes if it's already there
        db.query('INSERT INTO multiphase_%i VALUES (?, ?, ?)' % phase, (depth, TARGET_POS[phase], json.dumps([])))
    except IntegrityError:
        pass

    inserted = True

    # Third phase requires special condition due to sheer size of table
    if phase != 3 or depth != 0:
        while inserted:
            gc.collect()
            try:
                # Get loop condition and next depth of iteration from function - adding to DB as byproduct of assignment
                inserted, depth = generate_next_depth(db, depth, phase, verbose)
            except AssertionError as err:
                print(err)
    else:
        for move in MOVE_GROUPS_MASTER[phase]:
            depth = 0
            move_groups[phase] = [move]

            while inserted:
                gc.collect()
                try:
                    # Get loop condition and next depth of iteration from function -
                    # adding to DB as byproduct of assignment
                    inserted, depth = generate_next_depth(db, depth, phase, verbose)
                    # Reset move_group phase to full capacity after first depth
                    if phase == 3 and depth == 1:
                        move_groups[phase] = MOVE_GROUPS_MASTER[phase]
                except AssertionError as err:
                    print(err)


def generate_next_depth(db, depth, phase, verbose):
    """
    Generates the next depth level of positions in the database table by iterating through the previous depth
    :param db: Database Cursor object
    :param depth: the current depth level which has already been generated
    :param phase: current phase number, determines which table is being used
    :param verbose: Boolean to change output verbosity
    :return: boolean flag to state if any data has been inserted; the new max depth value
    """

    # Set of all positions for duplication checking. Uses more memory but greatly optimises processing time
    position_set = gen_position_set(db, depth, phase)
    start_time = int(round(time.time() * 1000))
    depth += 1
    print('%2i' % depth, end='.') if verbose else 0

    """
    Create an iterable to be processed by the Pool. It is structured like this:
    [(position String, move_sequence List), phaseInteger, position_set]
    """
    iterable = map(lambda e: (e, phase, position_set, move_groups),
                   db.query('SELECT position, move_sequence FROM multiphase_%i '
                            'where depth = %i' % (phase, depth - 1)).fetchall())
    print('.', end='') if verbose else 0

    # Create a MP Pool and give it the iterable to process across all CPU cores for most efficient processing
    p = Pool(processes=cpu_count())
    pool_result = p.starmap(generate_pos_children, iterable)
    p.close()
    gc.collect()
    print('.', end='') if verbose else 0
    insert_count = 0
    duplication_count = 0

    # Pool returns one list per process (effectively 2D array), which must be iterated through and added to DB
    for result_list in pool_result:
        result_list_length = len(result_list)
        for r in range(result_list_length):
            try:
                # Pop results to reduce memory and try to insert into DB
                result = result_list.pop()
                db.query('INSERT INTO multiphase_%i VALUES (?, ?, ?)' % phase,
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
    end_time = int(round(time.time() * 1000))
    total = (end_time - start_time) / 1000
    if verbose:
        print('.   Time: %10.3fs' % total, end='  |  ')
        print('DB Size: %7.2fMB' % (os.path.getsize('Codebase/database/db.sqlite') / 1000000), end='  |  ')
        print('Rows Added: %10i' % insert_count, end='  |  ')
        print('Duplications: %8i' % duplication_count)
    # need to include duplication count in case of resume with full depth
    return (insert_count + duplication_count > 0), depth


def gen_position_set(db, depth, phase):
    """
    Take all of the positions in the Database and put them into one set for quick duplication checking to reduce
    memory usage
    :param phase: The current phase being generated
    :param db: Database cursor object
    :param depth: Current depth
    :return: Set of position strings
    """
    position_set = set()

    try:
        result = db.query('SELECT position FROM multiphase_%i WHERE depth <= %i' % (phase, depth)).fetchall()
        for r in result:
            position_set.add(r[0])
    except OperationalError:
        # OperationalError if the table doesn't exist (or other SQLite errors)
        pass

    return position_set


def generate_pos_children(pos_tuple, phase, position_set, move_group_param):
    """
    Generate the children of a position by using the moves defined in the constant MOVES
    :param pos_tuple: tuple of position data: (position String, move_sequence List)
    :param phase: the current phase number for use in referencing the constant list indexes
    :param position_set: the large set must be passed in because the processes do not share memory
    :param move_group_param: the group of moves to be applied to the Cube
    :return: The list of new position data: [(position String, new move_sequence Serialized), (... ]
    """

    result_list = []
    for m in move_group_param[phase]:
        c = Cube(pos_tuple[0], True)
        dyn_move(c, m)

        if c.position not in position_set:
            result_list.append((c.position, json.loads(pos_tuple[1]) + [m.value]))

    return result_list
