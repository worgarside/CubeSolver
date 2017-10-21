from cube.color_class import Color
from cube.cube_class import Cube
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

SOLVED_CUBE = Cube(SOLVED_POS)


MOVES = ['u', 'not_u', 'u2', 'd', 'not_d', 'd2', 'l', 'not_l', 'l2', 'r', 'not_r', 'r2', 'f', 'not_f', 'f2', 'b',
         'not_b', 'b2', 'm', 'not_m', 'm2', 'e', 'not_e', 'e2', 's', 'not_s', 's2', 'x', 'not_x', 'y', 'not_y',
         'z', 'not_z']

SEARCH_MOVES = ['u', 'not_u', 'u2', 'd', 'not_d', 'd2', 'l', 'not_l', 'l2', 'r', 'not_r', 'r2', 'f', 'not_f', 'f2', 'b',
          'not_b', 'b2']

SUPERFLIP = ['r', 'l', 'u2', 'f', 'not_u', 'd', 'f2', 'r2', 'b2', 'l', 'u2',
             'not_f', 'not_b', 'u', 'r2', 'd', 'f2', 'u', 'r2', 'u']

SCRAMBLE = ['u', 'd', 'l', 'd2', 'r2', 'not_d', 'b2', 'r', 'u', 'not_b', 'r', 'l2']
