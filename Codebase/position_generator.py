from linked_list import LinkedList
from cube.move_class import Move as MOVE
from cube.moves import *
from cube.cube_class import Cube

DEPTH_LIMIT = 5

positions = {} # depth: set(position)

def generate_positions(cube, group):
    pos_list = LinkedList()

    depth = 0
    id = 0

    pos_list.push(id, cube.pos, MOVE.NONE, depth)
    positions[depth] = {cube.pos}

    while depth < DEPTH_LIMIT:
        positions[depth+1] = set()
        for p in positions[depth]:
            for m in group:
                c = Cube(p)
                u(c)
                positions[depth + 1].add(c.pos)

        depth += 1





        # pos_list.push(id, cube.pos, MOVE.U, depth)
        # depth += 1
        # print(depth, end=' ')

    print(positions)
