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
    color_dict = {'O': curses.COLOR_MAGENTA, 'R': curses.COLOR_RED, 'B': curses.COLOR_BLUE, 'Y': curses.COLOR_YELLOW,
                  'G': curses.COLOR_GREEN}
    position_set = set()

    curses.initscr()
    curses.start_color()

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)

                if c.position not in position_set:
                    id += 1
                    positions[depth + 1].append(Position(id, c.position, depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]]))
                    position_set.add(c.position)

                    if id % 193 == 0:
                        wrapper(print_status, depth, id, c.position, p.move_chain + [str(m)[5:]], color_dict)

                    if c.position == SOLVED_POS:
                        solved = True
                        solution_id = id
                        solution_move_chain = p.move_chain + [str(m)[5:]]
                        break
            if solved:
                break
        depth += 1

    wrapper(print_status, depth, solution_id, SOLVED_POS,solution_move_chain, color_dict)


def print_status(screen, depth, id, position, move_chain, color_dict):
    curses.init_pair(curses.COLOR_MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    screen.addstr(1, 0, "Depth: %i" % depth)
    screen.addstr(2, 0, "Current Position #%i" % id)
    screen.addstr(3, 0, "Move Chain: %s                 " % move_chain)
    addstr_colored(screen, 5, 8, " ".join(position[:3]), color_dict)
    addstr_colored(screen, 6, 8, " ".join(position[3:6]), color_dict)
    addstr_colored(screen, 7, 8, " ".join(position[6:9]), color_dict)
    addstr_colored(screen, 8, 2, " ".join(position[9:21]), color_dict)
    addstr_colored(screen, 9, 2, " ".join(position[21:33]), color_dict)
    addstr_colored(screen, 10, 2, " ".join(position[33:45]), color_dict)
    addstr_colored(screen, 11, 8, " ".join(position[45:48]), color_dict)
    addstr_colored(screen, 12, 8, " ".join(position[48:51]), color_dict)
    addstr_colored(screen, 13, 8, " ".join(position[51:]), color_dict)
    screen.refresh()


def addstr_colored(screen, row, col, string, color_dict):
    screen.move(row, col)

    pattern = r'([A-Z])'
    s = re.split(pattern, string)
    for s in s:
        screen.addstr(s, curses.color_pair(color_dict.get(s, 0)))
