from side_class import Side
from rotation_class import Rotation
import data
import primary_moves as pmove
from copy import deepcopy
import solver


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
        self._white_side = None
        self._yellow_side = None
        self._green_side = None
        self._blue_side = None
        self._red_side = None
        self._orange_side = None
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

    # Updates the sides of the cube from the main position variable
    def update_sides(self):
        self.up = self._pos[:9]
        self.down = self._pos[45:54]
        self.left = self._pos[9:12] + self._pos[21:24] + self._pos[33:36]
        self.right = self._pos[15:18] + self._pos[27:30] + self._pos[39:42]
        self.front = self._pos[12:15] + self._pos[24:27] + self._pos[36:39]
        self.back = self._pos[18:21] + self._pos[30:33] + self._pos[42:45]

        self.set_color_sides()

    # Sets the colored side variables for use in move conversion
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
            setattr(self, '_' + str(value.lower()) + '_side', Side[key])

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

    # Generates main solves sequence then processes it from human to robot
    def generate_solve_sequences(self):
        # runs solve functions to produce sequence of digital moves to generate_solve_sequences
        self.digital_solve_sequence = solver.solve(self)
        print('\n')
        self.normalize_digital_move_sequence()
        self.convert_digital_to_colors()
        self.create_robot_solve_sequence()

    # Changes digital/human moves to account for frame of reference changes with M/E/S robot style moves
    def normalize_digital_move_sequence(self):
        temp_sequence = self.digital_solve_sequence
        for index, move in enumerate(temp_sequence):
            norm_dict = {
                'm': self.norm_m,
                'not_m': self.norm_not_m,
                'm2': self.norm_m2,
                'e': self.norm_e,
                'not_e': self.norm_not_e,
                'e2': self.norm_e2,
                's': self.norm_s,
                'not_s': self.norm_not_s,
                's2': self.norm_s2,
            }

            temp_sequence = temp_sequence[:index+1] + norm_dict.get(move, self.norm_default)(temp_sequence[index+1:])
        self.digital_solve_sequence = temp_sequence

    def optimize_digital_move_sequence(self):
        # combine repeated moves
        # eliminate consecutive opposite moves
        pass

    """
    Converts each of the SIDE based moves into COLOR based moves
    This means that even though the robot rotates the cube in order to perform 
    certain moves, the frame of reference remains unchanged
    """
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

        for move in self.digital_solve_sequence:
            for color in move_to_color_dict[move]:
                self.color_solve_sequence.append(color.lower())

    # Uses the primary, secondary and tertiary move levels to create a robot-usable move sequence
    def create_robot_solve_sequence(self):
        temp_cube = deepcopy(self)
        for index, pm in enumerate(temp_cube.color_solve_sequence):
            method = getattr(pmove, pm)
            method(temp_cube)
            self.robot_solve_sequence = temp_cube.robot_solve_sequence

    # Static methods to normalize a sequence passed to it from the main normalize method
    @staticmethod
    def norm_default(sequence):
        return sequence

    @staticmethod
    def norm_m(sequence):
        move_m_dict = {
            'u': 'b',
            'not_u': 'not_b',
            'u2': 'b2',
            'd': 'f',
            'not_d': 'not_f',
            'd2': 'f2',
            'l': 'l',
            'not_l': 'not_l',
            'l2': 'l2',
            'r': 'r',
            'not_r': 'not_r',
            'r2': 'r2',
            'f': 'u',
            'not_f': 'not_u',
            'f2': 'u2',
            'b': 'd',
            'not_b': 'not_d',
            'b2': 'd2',
            'm': 'm',
            'not_m': 'not_m',
            'm2': 'm2',
            'e': 's',
            'not_e': 'not_s',
            'e2': 's2',
            's': 'not_e',
            'not_s': 'e',
            's2': 'e2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_m_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_not_m(sequence):
        move_not_m_dict = {
            'u': 'f',
            'not_u': 'not_f',
            'u2': 'f2',
            'd': 'b',
            'not_d': 'not_b',
            'd2': 'b2',
            'l': 'l',
            'not_l': 'not_l',
            'l2': 'l2',
            'r': 'r',
            'not_r': 'not_r',
            'r2': 'r2',
            'f': 'd',
            'not_f': 'not_d',
            'f2': 'd2',
            'b': 'u',
            'not_b': 'not_u',
            'b2': 'u2',
            'm': 'm',
            'not_m': 'not_m',
            'm2': 'm2',
            'e': 'not_s',
            'not_e': 's',
            'e2': 's2',
            's': 'not_e',
            'not_s': 'e',
            's2': 'e2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_not_m_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_m2(sequence):
        move_m2_dict = {
            'u': 'd',
            'not_u': 'not_d',
            'u2': 'd2',
            'd': 'u',
            'not_d': 'not_u',
            'd2': 'u2',
            'l': 'l',
            'not_l': 'not_l',
            'l2': 'l2',
            'r': 'r',
            'not_r': 'not_r',
            'r2': 'r2',
            'f': 'b',
            'not_f': 'not_b',
            'f2': 'b2',
            'b': 'f',
            'not_b': 'not_f',
            'b2': 'f2',
            'm': 'm',
            'not_m': 'not_m',
            'm2': 'm2',
            'e': 'not_e',
            'not_e': 'e',
            'e2': 'e2',
            's': 'not_s',
            'not_s': 's',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_m2_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_e(sequence):
        move_e_dict = {
            'u': 'u',
            'not_u': 'not_u',
            'u2': 'u2',
            'd': 'd',
            'not_d': 'not_d',
            'd2': 'd2',
            'l': 'b',
            'not_l': 'not_b',
            'l2': 'b2',
            'r': 'f',
            'not_r': 'not_f',
            'r2': 'f2',
            'f': 'l',
            'not_f': 'not_l',
            'f2': 'l2',
            'b': 'r',
            'not_b': 'not_r',
            'b2': 'r2',
            'm': 'not_s',
            'not_m': 's',
            'm2': 's2',
            'e': 'e',
            'not_e': 'not_e',
            'e2': 'e2',
            's': 'm',
            'not_s': 'not_m',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_e_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_not_e(sequence):
        move_not_e_dict = {
            'u': 'f',
            'not_u': 'not_f',
            'u2': 'f2',
            'd': 'b',
            'not_d': 'not_b',
            'd2': 'b2',
            'l': 'l',
            'not_l': 'not_l',
            'l2': 'l2',
            'r': 'r',
            'not_r': 'not_r',
            'r2': 'r2',
            'f': 'd',
            'not_f': 'not_d',
            'f2': 'd2',
            'b': 'u',
            'not_b': 'not_u',
            'b2': 'u2',
            'm': 'not_s',
            'not_m': 's',
            'm2': 'm2',
            'e': 'e',
            'not_e': 'not_e',
            'e2': 'e2',
            's': 'm',
            'not_s': 'not_m',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_not_e_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_e2(sequence):
        move_e2_dict = {
            'u': 'd',
            'not_u': 'not_d',
            'u2': 'd2',
            'd': 'u',
            'not_d': 'not_u',
            'd2': 'u2',
            'l': 'l',
            'not_l': 'not_l',
            'l2': 'l2',
            'r': 'r',
            'not_r': 'not_r',
            'r2': 'r2',
            'f': 'b',
            'not_f': 'not_b',
            'f2': 'b2',
            'b': 'f',
            'not_b': 'not_f',
            'b2': 'f2',
            'm': 'not_m',
            'not_m': 'm',
            'm2': 'm2',
            'e': 'e',
            'not_e': 'not_e',
            'e2': 'e2',
            's': 'not_s',
            'not_s': 's',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_e2_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_s(sequence):
        move_s_dict = {
            'u': 'l',
            'not_u': 'not_l',
            'u2': 'l2',
            'd': 'r',
            'not_d': 'not_r',
            'd2': 'r2',
            'l': 'd',
            'not_l': 'not_d',
            'l2': 'd2',
            'r': 'u',
            'not_r': 'not_u',
            'r2': 'u2',
            'f': 'f',
            'not_f': 'not_f',
            'f2': 'f2',
            'b': 'b',
            'not_b': 'not_b',
            'b2': 'b2',
            'm': 'e',
            'not_m': 'not_e',
            'm2': 'e2',
            'e': 'not_m',
            'not_e': 'm',
            'e2': 'e2',
            's': 's',
            'not_s': 'not_s',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_s_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_not_s(sequence):
        move_not_s_dict = {
            'u': 'r',
            'not_u': 'not_r',
            'u2': 'r2',
            'd': 'l',
            'not_d': 'not_l',
            'd2': 'l2',
            'l': 'u',
            'not_l': 'not_u',
            'l2': 'u2',
            'r': 'd',
            'not_r': 'not_d',
            'r2': 'd2',
            'f': 'f',
            'not_f': 'not_f',
            'f2': 'f2',
            'b': 'b',
            'not_b': 'not_b',
            'b2': 'b2',
            'm': 'not_e',
            'not_m': 'e',
            'm2': 'e2',
            'e': 'm',
            'not_e': 'not_m',
            'e2': 'e2',
            's': 's',
            'not_s': 'not_s',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_not_s_dict[sequence[i]]
        return sequence

    @staticmethod
    def norm_s2(sequence):
        move_s2_dict = {
            'u': 'd',
            'not_u': 'not_d',
            'u2': 'd2',
            'd': 'u',
            'not_d': 'not_u',
            'd2': 'u2',
            'l': 'r',
            'not_l': 'not_r',
            'l2': 'r2',
            'r': 'l',
            'not_r': 'not_l',
            'r2': 'l2',
            'f': 'f',
            'not_f': 'not_f',
            'f2': 'f2',
            'b': 'b',
            'not_b': 'not_b',
            'b2': 'b2',
            'm': 'not_m',
            'not_m': 'm',
            'm2': 'm2',
            'e': 'not_e',
            'not_e': 'e',
            'e2': 'e2',
            's': 's',
            'not_s': 'not_s',
            's2': 's2'
        }
        for i in range(len(sequence)):
            sequence[i] = move_s2_dict[sequence[i]]
        return sequence
