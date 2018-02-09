# #!/usr/bin/env python
import curses
from curses import wrapper
import re
#
#
# def addstr_colorized(win, y, x, s):
#     colors = {'G': curses.COLOR_GREEN, 'R': curses.COLOR_RED}
#     win.move(y, x)
#     pattern = r'([A-Z])'
#     s = re.split(pattern, s)
#     for s in s:
#         win.addstr(s, curses.color_pair(colors.get(s, 0)))
#
#
def main(stdscr, colors):


    addstr_colorized(stdscr, 4, 0, "WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY", colors)
    stdscr.refresh()



def print_status(screen, depth, id, position, move_chain, color_dict):
    curses.init_pair(curses.COLOR_MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    screen.addstr(1, 0, "Depth: %i" % depth)
    screen.addstr(2, 0, "Current Position #%i" % id)
    addstr_colorized(screen, 3, 0, position, color_dict)

    # screen.addstr(3, 0, "Position: ")

    screen.addstr(4, 0, "Move Chain: %s                 " % move_chain)
    screen.refresh()


def addstr_colorized(win, y, x, s, color_dict):
    win.move(y, x)

    pattern = r'([A-Z])'
    s = re.split(pattern, s)
    for s in s:
        win.addstr(s, curses.color_pair(color_dict.get(s, 0)))

curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()

color_dict = {'O': curses.COLOR_MAGENTA, 'R': curses.COLOR_RED, 'B': curses.COLOR_BLUE, 'Y': curses.COLOR_YELLOW, 'G': curses.COLOR_GREEN}

wrapper(print_status, 1, 420, "WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY", ['NOT_L', 'NOT_R', 'NOT_U'], colors)
# wrapper(main, colors)
