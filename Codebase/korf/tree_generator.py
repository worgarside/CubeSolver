from cube.cube_class import Cube, SOLVED_POS
from korf.position_class import Position # (id, position, depth, parent_id, parent_move, move_chain)
from cube.move_class import Move as MOVE
from cube.moves import dyn_move
import curses

def generator(cube, move_group):
    global stdscr
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

    while not solved:
        positions[depth + 1] = []
        for p in positions[depth]:
            for m in move_group:
                c = Cube(p.position)
                dyn_move(c, m)
                id += 1
                positions[depth + 1].append(Position(id, c.position, depth + 1, p.id, str(m), p.move_chain + [str(m)[5:]]))

                if id % 47 == 0:
                    print_status(depth, id, c.position, p.move_chain + [str(m)[5:]])

                if c.position == SOLVED_POS:
                    solved = True
                    solution_id = id
                    solution_move_chain = p.move_chain + [str(m)[5:]]
                    break
            if solved:
                break
        depth += 1

    print_status(depth, solution_id, SOLVED_POS, solution_move_chain)

    # curses.echo()
    # curses.nocbreak()
    # curses.endwin()
    # sys.stdout.write("\rDepth: %i     Pos ID: %i     Cube: %s     Move Chain: %s                         " %
    #                  (depth, solution_id, SOLVED_POS, solution_move_chain))
    # sys.stdout.flush()

def print_status(depth, id, position, move_chain):
    stdscr.addstr(0, 0, "Depth: %i" % depth)
    stdscr.addstr(1, 0, "Current Position #%i" % id)
    stdscr.addstr(2, 0, "Position: %s" % position)
    stdscr.addstr(3, 0, "Move Chain: %s                 " % move_chain)
    stdscr.addstr(4, 0, "")
    stdscr.refresh()