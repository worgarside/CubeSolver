from color_class import Color

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

MOVES8 = ['m', 'e2', 'not_f', 'not_m', 'e2', 'l2', 'l', 'not_s', 'l2', 'd2', 'u', 'u2', 'not_e', 'l2', 'f', 'b2', 'u2', 'f', 'not_d', 'l', 'u', 'u', 'e2', 'd', 'b', 'b', 'r2', 'f', 'd2', 's']

MOVES9 = ['m', 'e2', 'not_f']#, 'not_m', 'e2', 'l2']
