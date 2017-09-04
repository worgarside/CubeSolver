from side_class import Side
from rotation_class import Rotation
import data


class Cube:
    """A Rubik's Cube with 54 different coloured tiles"""

    # constructor
    def __init__(self, pos):
        self._pos = pos
        self.up = self._pos[:9]
        self.down = self._pos[45:54]
        self.left = self._pos[9:12] + self._pos[21:24] + self._pos[33:36]
        self.right = self._pos[15:18] + self._pos[27:30] + self._pos[39:42]
        self.front = self._pos[12:15] + self._pos[24:27] + self._pos[36:39]
        self.back = self._pos[18:21] + self._pos[30:33] + self._pos[42:45]
        self._white_face = None
        self._yellow_face = None
        self._green_face = None
        self._blue_face = None
        self._red_face = None
        self._orange_face = None
        self.color_side_dict = {}
        self.digital_solve_sequence = []
        self.color_solve_sequence = []
        self.robot_solve_sequence = []
        self.update_sides()

    def __str__(self):
        char_net = ''
        for i in self._pos:
            char_net = char_net + i.name[0]

        cube_net = '\n   ' + char_net[:3] + '\n   ' + char_net[3:6] + '\n   ' + char_net[6:9] + \
                   '\n' + char_net[9:21] + '\n' + char_net[21:33] + '\n' + char_net[33:45] + \
                   '\n   ' + char_net[45:48] + '\n   ' + char_net[48:51] + '\n   ' + char_net[51:54]

        cube_net_spaced = ''
        for letter in cube_net:
            cube_net_spaced += ' ' + letter

        return cube_net_spaced

    # Updates the sides of the cube to ensure they all match up
    def update_sides(self):
        self.up = self._pos[:9]
        self.down = self._pos[45:54]
        self.left = self._pos[9:12] + self._pos[21:24] + self._pos[33:36]
        self.right = self._pos[15:18] + self._pos[27:30] + self._pos[39:42]
        self.front = self._pos[12:15] + self._pos[24:27] + self._pos[36:39]
        self.back = self._pos[18:21] + self._pos[30:33] + self._pos[42:45]

        self.set_color_sides()

    def set_color_sides(self):
        self.color_side_dict = {
            'UP': self.up[4].name,
            'DOWN': self.down[4].name,
            'LEFT': self.left[4].name,
            'RIGHT': self.right[4].name,
            'FRONT': self.front[4].name,
            'BACK': self.back[4].name
        }

        for key, value in self.color_side_dict.items():
            setattr(self, str(value.lower()) + '_face', Side[key])

    # Setter methods
    def set_up(self, pos):
        if len(pos) == 9:
            self._pos = pos + self._pos[9:]
            self.update_sides()
        else:
            print('\nset_up: len(pos) != 9')
            exit()

    def set_down(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:45] + pos
            self.update_sides()
        else:
            print('\nset_down: len(pos) != 9')
            exit()

    def set_left(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:9] + pos[:3] + self._pos[12:21] + pos[3:6] + self._pos[24:33] + pos[6:] +\
                        self._pos[36:]
            self.update_sides()
        else:
            print('\nset_left: len(pos) != 9')
            exit()

    def set_right(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:15] + pos[:3] + self._pos[18:27] + pos[3:6] + self._pos[30:39] + pos[6:] +\
                        self._pos[42:]
            self.update_sides()
        else:
            print('\nset_right: len(pos) != 9')
            exit()

    def set_front(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:12] + pos[:3] + self._pos[15:24] + pos[3:6] + self._pos[27:36] + pos[6:] +\
                        self._pos[39:]
            self.update_sides()
        else:
            print('\nset_front: len(pos) != 9')
            exit()

    def set_back(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:18] + pos[:3] + self._pos[21:30] + pos[3:6] + self._pos[33:42] + pos[6:] +\
                        self._pos[45:]
            self.update_sides()
        else:
            print('\nset_back: len(pos) != 9')
            exit()

    def rotate_side(self, direction, side):
        c = Cube(self._pos)

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

    def solve(self):
        # runs solve functions to produce sequence of digital moves to solve
        self.digital_solve_sequence = data.MOVES5
        self.convert_digital_to_colors()

    def convert_digital_to_colors(self):
        move_to_color_dict = {
            'u': [self.color_side_dict['UP']],
            'not_u': ['not_' + self.color_side_dict['UP']],
            'u2': [self.color_side_dict['UP'] + '2'],
            'd': [self.color_side_dict['DOWN']],
            'not_d': ['not_' + self.color_side_dict['DOWN']],
            'd2': [self.color_side_dict['DOWN'] + '2'],
            'l': [self.color_side_dict['LEFT']],
            'not_l': ['not_' + self.color_side_dict['LEFT']],
            'l2': [self.color_side_dict['LEFT'] + '2'],
            'r': [self.color_side_dict['RIGHT']],
            'not_r': ['not_' + self.color_side_dict['RIGHT']],
            'r2': [self.color_side_dict['RIGHT'] + '2'],
            'f': [self.color_side_dict['FRONT']],
            'not_f': ['not_' + self.color_side_dict['FRONT']],
            'f2': [self.color_side_dict['FRONT'] + '2'],
            'b': [self.color_side_dict['BACK']],
            'not_b': ['not_' + self.color_side_dict['BACK']],
            'b2': [self.color_side_dict['BACK'] + '2'],
            'm': [self.color_side_dict['RIGHT'], 'not_' + self.color_side_dict['LEFT']],
            'not_m': ['not_' + self.color_side_dict['RIGHT'], self.color_side_dict['LEFT']],
            'm2': [self.color_side_dict['RIGHT'] + '2', self.color_side_dict['LEFT'] + '2'],
            'e': [self.color_side_dict['UP'], 'not_' + self.color_side_dict['DOWN']],
            'not_e': ['not_' + self.color_side_dict['UP'], self.color_side_dict['DOWN']],
            'e2': [self.color_side_dict['UP'] + '2', self.color_side_dict['DOWN'] + '2'],
            's': ['not_' + self.color_side_dict['FRONT'], self.color_side_dict['BACK']],
            'not_s': [self.color_side_dict['FRONT'], 'not_' + self.color_side_dict['BACK']],
            's2': [self.color_side_dict['FRONT'] + '2', self.color_side_dict['BACK'] + '2']
        }

        for m in self.digital_solve_sequence:
            for c in move_to_color_dict[m]:
                self.color_solve_sequence.append(c.lower())
