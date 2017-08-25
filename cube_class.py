from enum import Enum
import random


class Side(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    FRONT = 4
    BACK = 5


class Rot(Enum):
    CLOCKWISE = 0
    COUNTER_CLOCKWISE = 1


class Color(Enum):
    NONE = 0
    DARK = 1  # DARK (not 'BLACK') to show up with any color reading errors (differentiates it from BLUE)
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5
    WHITE = 6
    ORANGE = 7  # Color Sensor actually reads Brown


class Cube:
    """A Rubik's Cube with 54 different coloured tiles"""

    # Default cube position as a net, written as rows from up to down
    SOLVED_POS = [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE,
                  Color.WHITE, Color.WHITE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED,
                  Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN,
                  Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE,
                  Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED,
                  Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.YELLOW,
                  Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW,
                  Color.YELLOW]

    MOVES = ["l", "not_l", "l2", "r", "not_r", "r2", "u", "not_u", "u2", "d", "not_d", "d2", "f", "not_f", "f2", "b",
             "not_b", "b2", "m", "not_m", "m2", "e", "not_e", "e2", "s", "not_s", "s2", "x", "not_x", "y", "not_y",
             "z", "not_z"]
    MOVES2 = ["not_y", "l", "d2", "m", "not_d", "f", "x", "not_r", "m",
              "s2", "not_z", "d2", "e2", "not_z", "f2", "l", "not_x"]
    MOVES3 = ["not_y", "l", "d2", "r", "not_l", "x", "not_d", "f", "x",
              "not_l", "not_x", "f2", "b2", "z", "d2", "e2", "not_z", "f2", "l", "not_x"]

    # constructor
    def __init__(self, curr_pos):
        self._pos = curr_pos
        self.up = self._pos[:9]
        self.down = self._pos[45:54]
        self.left = self._pos[9:12] + self._pos[21:24] + self._pos[33:36]
        self.right = self._pos[15:18] + self._pos[27:30] + self._pos[39:42]
        self.front = self._pos[12:15] + self._pos[24:27] + self._pos[36:39]
        self.back = self._pos[18:21] + self._pos[30:33] + self._pos[42:45]

    # overrides print method to print net
    def __str__(self):
        char_net = ""
        for i in self._pos:
            char_net = char_net + i.name[0]

        cube_net = "\n   " + char_net[:3] + "\n   " + char_net[3:6] + "\n   " + char_net[6:9] + \
                   "\n" + char_net[9:21] + "\n" + char_net[21:33] + "\n" + char_net[33:45] + \
                   "\n   " + char_net[45:48] + "\n   " + char_net[48:51] + "\n   " + char_net[51:54]

        cube_net_spaced = ""
        for letter in cube_net:
            cube_net_spaced += " " + letter

        return cube_net_spaced

    # Updates the sides of the cube to ensure they all match up
    def update_sides(self):
        self.up = self._pos[:9]
        self.down = self._pos[45:54]
        self.left = self._pos[9:12] + self._pos[21:24] + self._pos[33:36]
        self.right = self._pos[15:18] + self._pos[27:30] + self._pos[39:42]
        self.front = self._pos[12:15] + self._pos[24:27] + self._pos[36:39]
        self.back = self._pos[18:21] + self._pos[30:33] + self._pos[42:45]

    # Setter methods
    def set_up(self, pos):
        if len(pos) == 9:
            self._pos = pos + self._pos[9:]
            self.update_sides()
        else:
            print("\nset_up: len(pos) != 9")
            exit()

    def set_down(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:45] + pos
            self.update_sides()
        else:
            print("\nset_down: len(pos) != 9")
            exit()

    def set_left(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:9] + pos[:3] + self._pos[12:21] + pos[3:6] + self._pos[24:33] + pos[6:] +\
                        self._pos[36:]
            self.update_sides()
        else:
            print("\nset_left: len(pos) != 9")
            exit()

    def set_right(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:15] + pos[:3] + self._pos[18:27] + pos[3:6] + self._pos[30:39] + pos[6:] +\
                        self._pos[42:]
            self.update_sides()
        else:
            print("\nset_right: len(pos) != 9")
            exit()

    def set_front(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:12] + pos[:3] + self._pos[15:24] + pos[3:6] + self._pos[27:36] + pos[6:] +\
                        self._pos[39:]
            self.update_sides()
        else:
            print("\nset_front: len(pos) != 9")
            exit()

    def set_back(self, pos):
        if len(pos) == 9:
            self._pos = self._pos[:18] + pos[:3] + self._pos[21:30] + pos[3:6] + self._pos[33:42] + pos[6:] +\
                        self._pos[45:]
            self.update_sides()
        else:
            print("\nset_back: len(pos) != 9")
            exit()

    def rotate_side(self, direction, side):
        c = Cube(self._pos)

        if direction == Rot.CLOCKWISE:
            if side == Side.LEFT:
                self.set_left(c.left[6] + c.left[3] + c.left[0] + c.left[7] + c.left[4]
                              + c.left[1] + c.left[8] + c.left[5] + c.left[2])
            elif side == Side.RIGHT:
                self.set_right(c.right[6] + c.right[3] + c.right[0] + c.right[7] + c.right[4]
                               + c.right[1] + c.right[8] + c.right[5] + c.right[2])
            elif side == Side.FRONT:
                self.set_front(c.front[6] + c.front[3] + c.front[0] + c.front[7] + c.front[4]
                               + c.front[1] + c.front[8] + c.front[5] + c.front[2])
            elif side == Side.BACK:
                self.set_back(c.back[6] + c.back[3] + c.back[0] + c.back[7] + c.back[4]
                              + c.back[1] + c.back[8] + c.back[5] + c.back[2])
            elif side == Side.UP:
                self.set_up(c.up[6] + c.up[3] + c.up[0] + c.up[7] + c.up[4]
                            + c.up[1] + c.up[8] + c.up[5] + c.up[2])
            elif side == Side.DOWN:
                self.set_down(c.down[6] + c.down[3] + c.down[0] + c.down[7] + c.down[4]
                              + c.down[1] + c.down[8] + c.down[5] + c.down[2])
            else:
                print("\nrotate_side_cw: invalid side")
                exit()
        elif direction == Rot.COUNTER_CLOCKWISE:

            if side == Side.LEFT:
                self.set_left(c.left[2] + c.left[5] + c.left[8] + c.left[1] + c.left[4]
                              + c.left[7] + c.left[0] + c.left[3] + c.left[6])
            elif side == Side.RIGHT:
                self.set_right(c.right[2] + c.right[5] + c.right[8] + c.right[1] + c.right[4]
                               + c.right[7] + c.right[0] + c.right[3] + c.right[6])
            elif side == Side.FRONT:
                self.set_front(c.front[2] + c.front[5] + c.front[8] + c.front[1] + c.front[4]
                               + c.front[7] + c.front[0] + c.front[3] + c.front[6])
            elif side == Side.BACK:
                self.set_back(c.back[2] + c.back[5] + c.back[8] + c.back[1] + c.back[4]
                              + c.back[7] + c.back[0] + c.back[3] + c.back[6])
            elif side == Side.UP:
                self.set_up(c.up[2] + c.up[5] + c.up[8] + c.up[1] + c.up[4]
                            + c.up[7] + c.up[0] + c.up[3] + c.up[6])
            elif side == Side.DOWN:
                self.set_down(c.down[2] + c.down[5] + c.down[8] + c.down[1] + c.down[4]
                              + c.down[7] + c.down[0] + c.down[3] + c.down[6])
            else:
                print("\nrotate_side_ccw: invalid side")
                exit()
        else:
            print("\nrotate_side: invalid direction")
            exit()

    # ######################## MOVES ######################## #
    
    def move_l(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.back[8] + c.up[1:3] + c.back[5] + c.up[4:6] + c.back[2] + c.up[7:])
        self.set_down(c.front[0] + c.down[1:3] + c.front[3] + c.down[4:6] + c.front[6] + c.down[7:])
        self.set_front(c.up[0] + c.front[1:3] + c.up[3] + c.front[4:6] + c.up[6] + c.front[7:])
        self.set_back(c.back[0:2] + c.down[6] + c.back[3:5] + c.down[3] + c.back[6:8] + c.down[0])
        self.rotate_side(Rot.CLOCKWISE, Side.LEFT)
        print("l") if print_flag else 0

    def move_not_l(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.front[0] + c.up[1:3] + c.front[3] + c.up[4:6] + c.front[6] + c.up[7:])
        self.set_down(c.back[8] + c.down[1:3] + c.back[5] + c.down[4:6] + c.back[2] + c.down[7:])
        self.set_front(c.down[0] + c.front[1:3] + c.down[3] + c.front[4:6] + c.down[6] + c.front[7:])
        self.set_back(c.back[0:2] + c.up[6] + c.back[3:5] + c.up[3] + c.back[6:8] + c.up[0])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.LEFT)
        print("l'") if print_flag else 0

    def move_l2(self, print_flag=False):
        self.move_l()
        self.move_l()
        print("l2") if print_flag else 0
        
    def move_r(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:2] + c.front[2] + c.up[3:5] + c.front[5] + c.up[6:8] + c.front[8])
        self.set_down(c.down[:2] + c.back[6] + c.down[3:5] + c.back[3] + c.down[6:8] + c.back[0])
        self.set_front(c.front[:2] + c.down[2] + c.front[3:5] + c.down[5] + c.front[6:8] + c.down[8])
        self.set_back(c.up[2] + c.back[1:3] + c.up[5] + c.back[4:6] + c.up[8] + c.back[7:])
        self.rotate_side(Rot.CLOCKWISE, Side.RIGHT)
        print("r") if print_flag else 0

    def move_not_r(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:2] + c.back[6] + c.up[3:5] + c.back[3] + c.up[6:8] + c.back[0])
        self.set_down(c.down[:2] + c.front[2] + c.down[3:5] + c.front[5] + c.down[6:8] + c.front[8])
        self.set_front(c.front[:2] + c.up[2] + c.front[3:5] + c.up[5] + c.front[6:8] + c.up[8])
        self.set_back(c.down[8] + c.back[1:3] + c.down[5] + c.back[4:6] + c.down[2] + c.back[7:])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.RIGHT)
        print("r'") if print_flag else 0

    def move_r2(self, print_flag=False):
        self.move_r()
        self.move_r()
        print("r2") if print_flag else 0

    def move_u(self, print_flag=False):
        c = Cube(self._pos)
        self.set_left(c.front[:3] + c.left[3:])
        self.set_right(c.back[:3] + c.right[3:])
        self.set_front(c.right[:3] + c.front[3:])
        self.set_back(c.left[:3] + c.back[3:])
        self.rotate_side(Rot.CLOCKWISE, Side.UP)
        print("u") if print_flag else 0

    def move_not_u(self, print_flag=False):
        c = Cube(self._pos)
        self.set_left(c.back[:3] + c.left[3:])
        self.set_right(c.front[:3] + c.right[3:])
        self.set_front(c.left[:3] + c.front[3:])
        self.set_back(c.right[:3] + c.back[3:])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.UP)
        print("u'") if print_flag else 0

    def move_u2(self, print_flag=False):
        self.move_u()
        self.move_u()
        print("u2") if print_flag else 0

    def move_d(self, print_flag=False):
        c = Cube(self._pos)
        self.set_left(c.left[:6] + c.back[6:])
        self.set_right(c.right[:6] + c.front[6:])
        self.set_front(c.front[:6] + c.left[6:])
        self.set_back(c.back[:6] + c.right[6:])
        self.rotate_side(Rot.CLOCKWISE, Side.DOWN)
        print("d") if print_flag else 0

    def move_not_d(self, print_flag=False):
        c = Cube(self._pos)
        self.set_left(c.left[:6] + c.front[6:])
        self.set_right(c.right[:6] + c.back[6:])
        self.set_front(c.front[:6] + c.right[6:])
        self.set_back(c.back[:6] + c.left[6:])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.DOWN)
        print("d'") if print_flag else 0

    def move_d2(self, print_flag=False):
        self.move_d()
        self.move_d()
        print("d2") if print_flag else 0

    def move_f(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:6] + c.left[8] + c.left[5] + c.left[2])
        self.set_down(c.right[6] + c.right[3] + c.right[0] + c.down[3:])
        self.set_left(c.left[:2] + c.down[0] + c.left[3:5] + c.down[1] + c.left[6:8] + c.down[2])
        self.set_right(c.up[6] + c.right[1:3] + c.up[7] + c.right[4:6] + c.up[8] + c.right[7:])
        self.rotate_side(Rot.CLOCKWISE, Side.FRONT)
        print("f") if print_flag else 0

    def move_not_f(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:6] + c.right[0] + c.right[3] + c.right[6])
        self.set_down(c.left[2] + c.left[5] + c.left[8] + c.down[3:])
        self.set_left(c.left[:2] + c.up[8] + c.left[3:5] + c.up[7] + c.left[6:8] + c.up[6])
        self.set_right(c.down[2] + c.right[1:3] + c.down[1] + c.right[4:6] + c.down[0] + c.right[7:])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.FRONT)
        print("f'") if print_flag else 0

    def move_f2(self, print_flag=False):
        self.move_f()
        self.move_f()
        print("f2") if print_flag else 0

    def move_b(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.right[2] + c.right[5] + c.right[8] + c.up[3:])
        self.set_down(c.down[:6] + c.left[0] + c.left[3] + c.left[6])
        self.set_left(c.up[2] + c.left[1:3] + c.up[1] + c.left[4:6] + c.up[0] + c.left[7:])
        self.set_right(c.right[:2] + c.down[8] + c.right[3:5] + c.down[7] + c.right[6:8] + c.down[6])
        self.rotate_side(Rot.CLOCKWISE, Side.BACK)
        print("b") if print_flag else 0

    def move_not_b(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.left[6] + c.left[3] + c.left[0] + c.up[3:])
        self.set_down(c.down[:6] + c.right[8] + c.right[5] + c.right[2])
        self.set_left(c.down[6] + c.left[1:3] + c.down[7] + c.left[4:6] + c.down[8] + c.left[7:])
        self.set_right(c.right[:2] + c.up[0] + c.right[3:5] + c.up[1] + c.right[6:8] + c.up[2])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.BACK)
        print("b'") if print_flag else 0

    def move_b2(self, print_flag=False):
        self.move_b()
        self.move_b()
        print("b2") if print_flag else 0

    def move_m(self, print_flag=False):
        self.move_r()
        self.move_not_l()
        self.move_not_x()
        print("m") if print_flag else 0

    def move_not_m(self, print_flag=False):
        self.move_not_r()
        self.move_l()
        self.move_x()
        print("m'") if print_flag else 0

    def move_m2(self, print_flag=False):
        self.move_m()
        self.move_m()
        print("m2") if print_flag else 0

    def move_e(self, print_flag=False):
        self.move_u()
        self.move_not_d()
        self.move_not_y()
        print("e") if print_flag else 0

    def move_not_e(self, print_flag=False):
        self.move_not_u()
        self.move_d()
        self.move_y()
        print("e'") if print_flag else 0

    def move_e2(self, print_flag=False):
        self.move_e()
        self.move_e()
        print("e2") if print_flag else 0

    def move_s(self, print_flag=False):
        self.move_not_f()
        self.move_b()
        self.move_z()
        print("s") if print_flag else 0

    def move_not_s(self, print_flag=False):
        self.move_f()
        self.move_not_b()
        self.move_not_z()
        print("s'") if print_flag else 0

    def move_s2(self, print_flag=False):
        self.move_s()
        self.move_s()
        print("s2") if print_flag else 0

    def move_x(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.front)
        self.set_down(c.back[::-1])  # [::-1] reverses the string
        self.set_front(c.down)
        self.set_back(c.up[::-1])  # [::-1] reverses the string
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.LEFT)
        self.rotate_side(Rot.CLOCKWISE, Side.RIGHT)
        print("x") if print_flag else 0

    def move_not_x(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.back[::-1])  # [::-1] reverses the string
        self.set_down(c.front)
        self.set_front(c.up)
        self.set_back(c.down[::-1])  # [::-1] reverses the string
        self.rotate_side(Rot.CLOCKWISE, Side.LEFT)
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.RIGHT)
        print("x'") if print_flag else 0

    def move_y(self, print_flag=False):
        c = Cube(self._pos)
        self.set_left(c.front)
        self.set_right(c.back)
        self.set_front(c.right)
        self.set_back(c.left)
        self.rotate_side(Rot.CLOCKWISE, Side.UP)
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.DOWN)
        print("y") if print_flag else 0

    def move_not_y(self, print_flag=False):
        c = Cube(self._pos)
        self.set_left(c.back)
        self.set_right(c.front)
        self.set_front(c.left)
        self.set_back(c.right)
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.UP)
        self.rotate_side(Rot.CLOCKWISE, Side.DOWN)
        print("y'") if print_flag else 0

    def move_z(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.left[6] + c.left[3] + c.left[0] + c.left[7] + c.left[4]
                    + c.left[1] + c.left[8] + c.left[5] + c.left[2])
        self.set_down(c.right[6] + c.right[3] + c.right[0] + c.right[7] + c.right[4]
                      + c.right[1] + c.right[8] + c.right[5] + c.right[2])
        self.set_left(c.down[6] + c.down[3] + c.down[0] + c.down[7] + c.down[4]
                      + c.down[1] + c.down[8] + c.down[5] + c.down[2])
        self.set_right(c.up[6] + c.up[3] + c.up[0] + c.up[7] + c.up[4] + c.up[1] + c.up[8] + c.up[5] + c.up[2])
        self.rotate_side(Rot.CLOCKWISE, Side.FRONT)
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.BACK)
        print("z") if print_flag else 0

    def move_not_z(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.right[2] + c.right[5] + c.right[8] + c.right[1]
                    + c.right[4] + c.right[7] + c.right[0] + c.right[3] + c.right[6])
        self.set_down(c.left[2] + c.left[5] + c.left[8] + c.left[1]
                      + c.left[4] + c.left[7] + c.left[0] + c.left[3] + c.left[6])
        self.set_left(c.up[2] + c.up[5] + c.up[8] + c.up[1] + c.up[4] + c.up[7] + c.up[0] + c.up[3] + c.up[6])
        self.set_right(c.down[2] + c.down[5] + c.down[8] + c.down[1]
                       + c.down[4] + c.down[7] + c.down[0] + c.down[3] + c.down[6])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.FRONT)
        self.rotate_side(Rot.CLOCKWISE, Side.BACK)
        print("z'") if print_flag else 0

    # ######################## MOVE IMPLEMENTERS ######################## #

    def move(self, move_string):
        try:
            move_func = self.__getattribute__("move_" + move_string)
            move_func(True)
        except AttributeError:
            print("\nmove(move_string): invalid move_string")
            exit()

    def follow_move_chain(self, move_chain):
        for move in move_chain:
            self.move(move)
            print(self)
            print("\n-----------")

    def randomize(self):
        number_of_moves = random.randint(10, 20)
        for n in range(number_of_moves):
            self.move(random.choice(Cube.MOVES))


def main():
    rubiks_cube = Cube(Cube.SOLVED_POS)
    print(rubiks_cube)
    # rubiks_cube.randomize()
    # print(rubiks_cube)


if __name__ == '__main__':
    main()
