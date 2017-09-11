from color_class import Color

"""
A file to hold constants for testing purposes, mainly to avoid cluttering up other classes
"""

# Default cube position as a net, written as rows from up to down
SOLVED_POS = [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE,
              Color.WHITE, Color.WHITE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED,
              Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN,
              Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE,
              Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED,
              Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.YELLOW,
              Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW,
              Color.YELLOW]

SOLVED_SIDES = [(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE,
                 Color.WHITE, Color.WHITE),
                (Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN,
                 Color.GREEN, Color.GREEN),
                (Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW,
                 Color.YELLOW, Color.YELLOW),
                (Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE,
                 Color.BLUE),
                (Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED),
                (Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE,
                 Color.ORANGE, Color.ORANGE)]

MOVES = ['u', 'not_u', 'u2', 'd', 'not_d', 'd2', 'l', 'not_l', 'l2', 'r', 'not_r', 'r2', 'f', 'not_f', 'f2', 'b',
         'not_b', 'b2', 'm', 'not_m', 'm2', 'e', 'not_e', 'e2', 's', 'not_s', 's2', 'x', 'not_x', 'y', 'not_y',
         'z', 'not_z']

MOVES1 = ['u', 'not_u', 'u2', 'd', 'not_d', 'd2', 'l', 'not_l', 'l2', 'r', 'not_r', 'r2', 'f', 'not_f', 'f2', 'b',
          'not_b', 'b2', 'm', 'not_m', 'm2', 'e', 'not_e', 'e2', 's', 'not_s', 's2']

MOVES2 = ['x', 'r', 'u2', 'd', 'not_z', 'not_b', 'f2', 'r2', 'd',
          'not_x', 'not_s', 'l2', 'y', 'not_r', 'not_f', 'm']

MOVES3 = ['r', 'u', 'not_r', 'u', 'r', 'u2', 'not_r']

MOVES4 = ['blue', 'white', 'not_blue', 'white', 'blue', 'white2', 'not_blue']

SUPERFLIP = ['r', 'l', 'u2', 'f', 'not_u', 'd', 'f2', 'r2', 'b2', 'l', 'u2',
             'not_f', 'not_b', 'u', 'r2', 'd', 'f2', 'u', 'r2', 'u']

MOVES5 = ['m2', 'u', 'm2', 'u2', 'm2', 'u', 'm2']

MOVES6 = ['m', 'u', 'm', 'u', 'm', 'u']

MOVES7 = ['m', 'e2', 'not_f', 'not_m', 'e2', 'l2', 'l', 'not_s', 'l2', 'd2', 'u', 'u2', 'not_e', 'l2', 'f']

MOVES8 = ['m', 'e2', 'not_f', 'not_m', 'e2', 'l2', 'l', 'not_s', 'l2', 'd2', 'u', 'u2', 'not_e', 'l2', 'f', 'b2',
          'u2', 'f', 'not_d', 'l', 'u', 'u', 'e2', 'd', 'b', 'b', 'r2', 'f', 'd2', 's']

MOVES9 = ['b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd', 'b', 'u', 'f', 'd']

MOVES10 = ['f', 'r2', 'u', 'not_r', 'l2', 'not_d', 'l', 'not_b', 'd2', 'e', 'r2', 'e2', 's2', 'u2', 'm']



MOVES10POS = [Color.YELLOW, Color.RED, Color.RED, Color.GREEN, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.WHITE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.YELLOW, Color.WHITE, Color.BLUE, Color.ORANGE, Color.YELLOW, Color.WHITE, Color.GREEN, Color.GREEN, Color.ORANGE, Color.BLUE, Color.BLUE, Color.WHITE, Color.BLUE, Color.YELLOW, Color.ORANGE, Color.BLUE, Color.GREEN, Color.BLUE, Color.YELLOW, Color.WHITE, Color.RED, Color.BLUE, Color.RED, Color.RED, Color.BLUE, Color.GREEN, Color.WHITE, Color.GREEN, Color.RED, Color.YELLOW, Color.GREEN, Color.ORANGE, Color.WHITE, Color.YELLOW, Color.YELLOW, Color.ORANGE, Color.YELLOW, Color.RED, Color.WHITE, Color.RED, Color.WHITE, Color.RED]
