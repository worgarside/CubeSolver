from cube.moves import *
from cube.cube_class import Cube
from position_class import Position # (id, position, depth, parent_id, parent_move)

DEPTH_LIMIT = 7

def generate_positions(db, cube, group):
    depth = 0
    id = 0

    db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)", (0, cube.position, depth, -1, 'NONE'))

    while depth < DEPTH_LIMIT:

        position_data = db.query("SELECT * FROM positions WHERE depth=?", [depth])
        position_data = position_data.fetchall()

        for p in position_data:
            for move in group:
                c = Cube(p[1])
                dyn_move(c, move)
                id += 1
                db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)", (id, c.position, depth+1, p[0], str(move)[5:]))

        depth += 1

                # found = db.query("SELECT EXISTS(SELECT 1 FROM positions WHERE position=?) LIMIT 1", [c.position]).fetchone()
                #
                # if found == (0,):
                #     id += 1
                #     db.query("INSERT INTO positions VALUES (?, ?, ?, ?, ?)", (id, c.position, depth, p[0], str(move)[5:]))
                #     print('-', end='')
                # else:
                #     print('.', end='')


def code_position(position):
    colors = []
    pos_coded = ""

    for color in position:
        if color not in colors:
            colors.append(color)

        pos_coded += str(colors.index(color))

    return pos_coded