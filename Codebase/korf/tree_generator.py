from cube.cube_class import Cube, SOLVED_POS
from korf.position_class import Position # (id, position, depth, parent_id, parent_move, move_chain)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move
import curses
import re
from curses import wrapper

def generator(cube, move_group):
    solved = False
    solution_id = -1
    positions = {}
    depth = 0
    id = 0
    positions[depth] = {Position(0, cube.position, depth, -1, MOVE.NONE, [])}
    solution_move_chain = []

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                id += 1
                positions[depth + 1].append(Position(id, c.position, depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]]))

                if id % 53 == 0:
                    print_status(stdscr, depth, id, c.position, p.move_chain + [str(m)[5:]])

                if c.position == SOLVED_POS:
                    solved = True
                    solution_id = id
                    solution_move_chain = p.move_chain + [str(m)[5:]]
                    break
            if solved:
                break
        depth += 1

    print_status(stdscr, depth, solution_id, SOLVED_POS,solution_move_chain)


def print_status(screen, depth, id, position, move_chain):
    screen.addstr(1, 0, "Depth: %i" % depth)
    screen.addstr(2, 0, "Current Position #%i" % id)
    screen.addstr(3, 0, "Move Chain: %s                 " % move_chain)
    screen.addstr(5, 8, " ".join(position[:3]))
    screen.addstr(6, 8, " ".join(position[3:6]))
    screen.addstr(7, 8, " ".join(position[6:9]))
    screen.addstr(8, 2, " ".join(position[9:21]))
    screen.addstr(9, 2, " ".join(position[21:33]))
    screen.addstr(10, 2, " ".join(position[33:45]))
    screen.addstr(11, 8, " ".join(position[45:48]))
    screen.addstr(12, 8, " ".join(position[48:51]))
    screen.addstr(13, 8, " ".join(position[51:]))



    screen.move(15, 0)
    screen.refresh()
