from .color_class import Color
from .rotation_class import Rotation
from .side_class import Side

SOLVED_POS = 'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY'
SOLVED_POS_REDUCED = 'WWWWWWWWWRRRBBBRRRBBBRRRBBBRRRBBBRRRBBBRRRBBBWWWWWWWWW'
SOLVED_SET = {'WWWWWWWWWOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY',
              'WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY',
              'WWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGYYYYYYYYY',
              'WWWWWWWWWBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRYYYYYYYYY',
              'OOOOOOOOOWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYGGGRRRRRRRRR',
              'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR',
              'OOOOOOOOOBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWRRRRRRRRR',
              'OOOOOOOOOYYYGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBRRRRRRRRR',
              'GGGGGGGGGWWWOOOYYYRRRWWWOOOYYYRRRWWWOOOYYYRRRBBBBBBBBB',
              'GGGGGGGGGOOOYYYRRRWWWOOOYYYRRRWWWOOOYYYRRRWWWBBBBBBBBB',
              'GGGGGGGGGRRRWWWOOOYYYRRRWWWOOOYYYRRRWWWOOOYYYBBBBBBBBB',
              'GGGGGGGGGYYYRRRWWWOOOYYYRRRWWWOOOYYYRRRWWWOOOBBBBBBBBB',
              'RRRRRRRRRWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYBBBOOOOOOOOO',
              'RRRRRRRRRGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWOOOOOOOOO',
              'RRRRRRRRRBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYOOOOOOOOO',
              'RRRRRRRRRYYYBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGOOOOOOOOO',
              'BBBBBBBBBWWWRRRYYYOOOWWWRRRYYYOOOWWWRRRYYYOOOGGGGGGGGG',
              'BBBBBBBBBOOOWWWRRRYYYOOOWWWRRRYYYOOOWWWRRRYYYGGGGGGGGG',
              'BBBBBBBBBRRRYYYOOOWWWRRRYYYOOOWWWRRRYYYOOOWWWGGGGGGGGG',
              'BBBBBBBBBYYYOOOWWWRRRYYYOOOWWWRRRYYYOOOWWWRRRGGGGGGGGG',
              'YYYYYYYYYOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGWWWWWWWWW',
              'YYYYYYYYYGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRWWWWWWWWW',
              'YYYYYYYYYRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBWWWWWWWWW',
              'YYYYYYYYYBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOWWWWWWWWW'}

EDGES = [(1, 19), (3, 10), (5, 16), (7, 13),
         (21, 32), (23, 24), (26, 27), (29, 30),
         (34, 48), (37, 46), (40, 50), (43, 52)]

EDGES_NO_UP_DOWN = [(19, 19), (10, 10), (16, 16), (13, 13),
         (21, 32), (23, 24), (26, 27), (29, 30),
         (34, 34), (37, 37), (40, 40), (43, 43)]


class Cube:
    def __init__(self, position=SOLVED_POS):
        self.position = position
        self.position_reduced = ''
        self.color_position = ''

        self.up = ''
        self.down = ''
        self.left = ''
        self.right = ''
        self.front = ''
        self.back = ''

        self.reduction_dict = {Color.ORANGE: Color.RED, Color.YELLOW: Color.WHITE, Color.GREEN: Color.BLUE,
                               Color.RED: Color.RED, Color.WHITE: Color.WHITE, Color.BLUE: Color.BLUE}
        self.opposite_sides_dict = {Side.UP: Side.DOWN, Side.DOWN: Side.UP, Side.LEFT: Side.RIGHT,
                                    Side.RIGHT: Side.LEFT, Side.FRONT: Side.BACK, Side.BACK: Side.FRONT}
        self.facelet_side_dict = {0: Side.UP, 1: Side.UP, 2: Side.UP, 3: Side.UP, 4: Side.UP, 5: Side.UP, 6: Side.UP,
                                  7: Side.UP, 8: Side.UP, 9: Side.LEFT, 10: Side.LEFT, 11: Side.LEFT, 12: Side.FRONT,
                                  13: Side.FRONT, 14: Side.FRONT, 15: Side.RIGHT, 16: Side.RIGHT, 17: Side.RIGHT,
                                  18: Side.BACK, 19: Side.BACK, 20: Side.BACK, 21: Side.LEFT, 22: Side.LEFT,
                                  23: Side.LEFT, 24: Side.FRONT, 25: Side.FRONT, 26: Side.FRONT, 27: Side.RIGHT,
                                  28: Side.RIGHT, 29: Side.RIGHT, 30: Side.BACK, 31: Side.BACK, 32: Side.BACK,
                                  33: Side.LEFT, 34: Side.LEFT, 35: Side.LEFT, 36: Side.FRONT, 37: Side.FRONT,
                                  38: Side.FRONT, 39: Side.RIGHT, 40: Side.RIGHT, 41: Side.RIGHT, 42: Side.BACK,
                                  43: Side.BACK, 44: Side.BACK, 45: Side.DOWN, 46: Side.DOWN, 47: Side.DOWN,
                                  48: Side.DOWN, 49: Side.DOWN, 50: Side.DOWN, 51: Side.DOWN, 52: Side.DOWN,
                                  53: Side.DOWN}
        self._color_print_dict = {Color.RED: '\033[31m', Color.BLUE: '\033[34m', Color.GREEN: '\033[32m',
                                  Color.ORANGE: '\033[35m', Color.WHITE: '\033[37m', Color.YELLOW: '\033[33m'}

        self.update_fields()

    def __str__(self):
        """ Returns a colored net of the Cube """
        linebreak_dict = {2: '\n      ', 5: '\n      ', 8: '\n', 20: '\n', 32: '\n', 44: '\n      ', 47: '\n      ',
                          50: '\n      '}
        char_net = '      '
        for index, color in enumerate(self.position):
            char_net += self._color_print_dict[Color(color)] + color + '\033[0m' + linebreak_dict.get(index, ' ')
        char_net += '\n'
        return char_net

    # ------------------ Update Methods ------------------ #

    def update_fields(self):
        """Updates all fields of Cube from position"""
        self.update_sides()
        self.update_pos_colors()
        self.update_reduced_cube()

    def update_sides(self):
        """ Updates the sides of the cube from the main position variable """
        self.up = self.position[:9]
        self.down = self.position[45:54]
        self.left = self.position[9:12] + self.position[21:24] + self.position[33:36]
        self.right = self.position[15:18] + self.position[27:30] + self.position[39:42]
        self.front = self.position[12:15] + self.position[24:27] + self.position[36:39]
        self.back = self.position[18:21] + self.position[30:33] + self.position[42:45]

    def update_pos_colors(self):
        """Updates position field with colored output"""
        self.color_position = ''
        for color in self.position:
            self.color_position += self._color_print_dict[Color(color)] + color + '\033[0m'

    def update_reduced_cube(self):
        self.position_reduced = ''
        for color in self.position:
            self.position_reduced += self.reduction_dict[Color(color)].value

    # ------------------ Setter Methods ------------------ #
    """Each of these sets the relevant face facelets to the given string and updates the relevant fields"""

    def set_up(self, pos):
        if len(pos) == 9:
            self.position = pos + self.position[9:]
            self.update_fields()
        else:
            print('\nset_up: len(position) != 9')
            exit()

    def set_down(self, pos):
        if len(pos) == 9:
            self.position = self.position[:45] + pos
            self.update_fields()
        else:
            print('\nset_down: len(position) != 9')
            exit()

    def set_left(self, pos):
        if len(pos) == 9:
            self.position = self.position[:9] + pos[:3] + self.position[12:21] + pos[3:6] + \
                            self.position[24:33] + pos[6:] + self.position[36:]
            self.update_fields()
        else:
            print('\nset_left: len(position) != 9')
            exit()

    def set_right(self, pos):
        if len(pos) == 9:
            self.position = self.position[:15] + pos[:3] + self.position[18:27] + pos[3:6] + \
                            self.position[30:39] + pos[6:] + self.position[42:]
            self.update_fields()
        else:
            print('\nset_right: len(position) != 9')
            exit()

    def set_front(self, pos):
        if len(pos) == 9:
            self.position = self.position[:12] + pos[:3] + self.position[15:24] + pos[3:6] + \
                            self.position[27:36] + pos[6:] + self.position[39:]
            self.update_fields()
        else:
            print('\nset_front: len(position) != 9')
            exit()

    def set_back(self, pos):
        if len(pos) == 9:
            self.position = self.position[:18] + pos[:3] + self.position[21:30] + pos[3:6] + \
                            self.position[33:42] + pos[6:] + self.position[45:]
            self.update_fields()
        else:
            print('\nset_back: len(position) != 9')
            exit()

    def rotate_side(self, direction, side):
        """Rotates the 9 facelets of a face"""
        c = Cube(self.position)

        if direction == Rotation.CLOCKWISE:
            if side == Side.LEFT:
                self.set_left(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.left[7:8] + c.left[4:5]
                              + c.left[1:2] + c.left[8:9] + c.left[5:6] + c.left[2:3])
            elif side == Side.RIGHT:
                self.set_right(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.right[7:8] + c.right[4:5]
                               + c.right[1:2] + c.right[8:9] + c.right[5:6] + c.right[2:3])
            elif side == Side.FRONT:
                self.set_front(c.front[6:7] + c.front[3:4] + c.front[0:1] + c.front[7:8] + c.front[4:5]
                               + c.front[1:2] + c.front[8:9] + c.front[5:6] + c.front[2:3])
            elif side == Side.BACK:
                self.set_back(c.back[6:7] + c.back[3:4] + c.back[0:1] + c.back[7:8] + c.back[4:5]
                              + c.back[1:2] + c.back[8:9] + c.back[5:6] + c.back[2:3])
            elif side == Side.UP:
                self.set_up(c.up[6:7] + c.up[3:4] + c.up[0:1] + c.up[7:8] + c.up[4:5]
                            + c.up[1:2] + c.up[8:9] + c.up[5:6] + c.up[2:3])
            elif side == Side.DOWN:
                self.set_down(c.down[6:7] + c.down[3:4] + c.down[0:1] + c.down[7:8] + c.down[4:5]
                              + c.down[1:2] + c.down[8:9] + c.down[5:6] + c.down[2:3])
            else:
                print('\nrotate_side_cw: invalid side')
                exit()
        elif direction == Rotation.COUNTER_CLOCKWISE:

            if side == Side.LEFT:
                self.set_left(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.left[1:2] + c.left[4:5]
                              + c.left[7:8] + c.left[0:1] + c.left[3:4] + c.left[6:7])
            elif side == Side.RIGHT:
                self.set_right(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.right[1:2] + c.right[4:5]
                               + c.right[7:8] + c.right[0:1] + c.right[3:4] + c.right[6:7])
            elif side == Side.FRONT:
                self.set_front(c.front[2:3] + c.front[5:6] + c.front[8:9] + c.front[1:2] + c.front[4:5]
                               + c.front[7:8] + c.front[0:1] + c.front[3:4] + c.front[6:7])
            elif side == Side.BACK:
                self.set_back(c.back[2:3] + c.back[5:6] + c.back[8:9] + c.back[1:2] + c.back[4:5]
                              + c.back[7:8] + c.back[0:1] + c.back[3:4] + c.back[6:7])
            elif side == Side.UP:
                self.set_up(c.up[2:3] + c.up[5:6] + c.up[8:9] + c.up[1:2] + c.up[4:5]
                            + c.up[7:8] + c.up[0:1] + c.up[3:4] + c.up[6:7])
            elif side == Side.DOWN:
                self.set_down(c.down[2:3] + c.down[5:6] + c.down[8:9] + c.down[1:2] + c.down[4:5]
                              + c.down[7:8] + c.down[0:1] + c.down[3:4] + c.down[6:7])
            else:
                print('\nrotate_side_ccw: invalid side')
                exit()
        else:
            print('\nrotate_side: invalid direction')
            exit()

    # ------------------ Getter Methods ------------------ #

    def get_color_of_side(self, **kwargs):
        if 'facelet' in kwargs:
            facelet = kwargs['facelet']
            try:
                side = self.facelet_side_dict[facelet]
                return Color(eval('self.%s' % side.name.lower())[4])
            except KeyError:
                print('Invalid Facelet number passed to method')

        if 'side' in kwargs:
            side = kwargs['side']
            try:
                return Color(eval('self.%s' % side.name.lower())[4])
            except AttributeError:
                print('Invalid Side passed to method')

    def get_side_with_color(self, **kwargs):
        if 'color' in kwargs:
            color = kwargs['color']
            sides = {Side.UP: self.up, Side.DOWN: self.down,
                     Side.LEFT: self.left, Side.RIGHT: self.right,
                     Side.FRONT: self.front, Side.BACK: self.back}

            for side, colors in sides.items():
                if Color(colors[4]) == color:
                    return side
            print("No sides found with color '%s'" % str(color))
            raise AttributeError
