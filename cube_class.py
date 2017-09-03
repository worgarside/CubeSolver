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
    ORANGE = 7  # Color Sensor actually reads BROWN


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

    MOVES = ["u", "not_u", "u2", "d", "not_d", "d2", "l", "not_l", "l2", "r", "not_r", "r2", "f", "not_f", "f2", "b",
             "not_b", "b2", "m", "not_m", "m2", "e", "not_e", "e2", "s", "not_s", "s2", "x", "not_x", "y", "not_y",
             "z", "not_z"]
    MOVES2 = ["x", "r", "u2", "d", "not_z", "not_b", "f2", "r2", "d",
              "not_x", "not_s", "l2", "y", "not_r", "not_f", "m"]

    MOVES3 = ["r", "u", "not_r", "u", "r", "u2", "not_r"]
    MOVES4 = ["blue", "white", "not_blue", "white", "blue", "white2", "not_blue"]


    # constructor
    def __init__(self, curr_pos):
        self._pos = curr_pos
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.front = None
        self.back = None
        self._white_face = None
        self._yellow_face = None
        self._green_face = None
        self._blue_face = None
        self._red_face = None
        self._orange_face = None

        self.update_sides()

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

        self.match_sides_colors()

    def match_sides_colors(self):
        up = self.up[4].name
        down = self.down[4].name
        left = self.left[4].name
        right = self.right[4].name
        front = self.front[4].name
        back = self.back[4].name

        if up.lower() == "white":
            self._white_face = Side.UP
        elif down.lower() == "white":
            self._white_face = Side.DOWN
        elif left.lower() == "white":
            self._white_face = Side.LEFT
        elif right.lower() == "white":
            self._white_face = Side.RIGHT
        elif front.lower() == "white":
            self._white_face = Side.FRONT
        elif back.lower() == "white":
            self._white_face = Side.BACK
        # else:
        #     print("ERROR #1")

        if up.lower() == "yellow":
            self._yellow_face = Side.UP
        elif down.lower() == "yellow":
            self._yellow_face = Side.DOWN
        elif left.lower() == "yellow":
            self._yellow_face = Side.LEFT
        elif right.lower() == "yellow":
            self._yellow_face = Side.RIGHT
        elif front.lower() == "yellow":
            self._yellow_face = Side.FRONT
        elif back.lower() == "yellow":
            self._yellow_face = Side.BACK
        # else:
        #     print("ERROR #2")

        if up.lower() == "green":
            self._green_face = Side.UP
        elif down.lower() == "green":
            self._green_face = Side.DOWN
        elif left.lower() == "green":
            self._green_face = Side.LEFT
        elif right.lower() == "green":
            self._green_face = Side.RIGHT
        elif front.lower() == "green":
            self._green_face = Side.FRONT
        elif back.lower() == "green":
            self._green_face = Side.BACK
        # else:
        #     print("ERROR #3")

        if up.lower() == "blue":
            self._blue_face = Side.UP
        elif down.lower() == "blue":
            self._blue_face = Side.DOWN
        elif left.lower() == "blue":
            self._blue_face = Side.LEFT
        elif right.lower() == "blue":
            self._blue_face = Side.RIGHT
        elif front.lower() == "blue":
            self._blue_face = Side.FRONT
        elif back.lower() == "blue":
            self._blue_face = Side.BACK
        # else:
        #     print("ERROR #4")

        if up.lower() == "red":
            self._red_face = Side.UP
        elif down.lower() == "red":
            self._red_face = Side.DOWN
        elif left.lower() == "red":
            self._red_face = Side.LEFT
        elif right.lower() == "red":
            self._red_face = Side.RIGHT
        elif front.lower() == "red":
            self._red_face = Side.FRONT
        elif back.lower() == "red":
            self._red_face = Side.BACK
        # else:
        #     print("ERROR #5")

        if up.lower() == "orange":
            self._orange_face = Side.UP
        elif down.lower() == "orange":
            self._orange_face = Side.DOWN
        elif left.lower() == "orange":
            self._orange_face = Side.LEFT
        elif right.lower() == "orange":
            self._orange_face = Side.RIGHT
        elif front.lower() == "orange":
            self._orange_face = Side.FRONT
        elif back.lower() == "orange":
            self._orange_face = Side.BACK
        # else:
        #     print("ERROR #6")

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
                print("\nrotate_side_cw: invalid side")
                exit()
        elif direction == Rot.COUNTER_CLOCKWISE:

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
                print("\nrotate_side_ccw: invalid side")
                exit()
        else:
            print("\nrotate_side: invalid direction")
            exit()

    # ######################## SIDE MOVES ######################## #

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

    def move_l(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.back[8:9] + c.up[1:3] + c.back[5:6] + c.up[4:6] + c.back[2:3] + c.up[7:])
        self.set_down(c.front[0:1] + c.down[1:3] + c.front[3:4] + c.down[4:6] + c.front[6:7] + c.down[7:])
        self.set_front(c.up[0:1] + c.front[1:3] + c.up[3:4] + c.front[4:6] + c.up[6:7] + c.front[7:])
        self.set_back(c.back[0:2] + c.down[6:7] + c.back[3:5] + c.down[3:4] + c.back[6:8] + c.down[0:1])
        self.rotate_side(Rot.CLOCKWISE, Side.LEFT)
        print("l") if print_flag else 0

    def move_not_l(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.front[0:1] + c.up[1:3] + c.front[3:4] + c.up[4:6] + c.front[6:7] + c.up[7:])
        self.set_down(c.back[8:9] + c.down[1:3] + c.back[5:6] + c.down[4:6] + c.back[2:3] + c.down[7:])
        self.set_front(c.down[0:1] + c.front[1:3] + c.down[3:4] + c.front[4:6] + c.down[6:7] + c.front[7:])
        self.set_back(c.back[0:2] + c.up[6:7] + c.back[3:5] + c.up[3:4] + c.back[6:8] + c.up[0:1])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.LEFT)
        print("l'") if print_flag else 0

    def move_l2(self, print_flag=False):
        self.move_l()
        self.move_l()
        print("l2") if print_flag else 0
        
    def move_r(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:2] + c.front[2:3] + c.up[3:5] + c.front[5:6] + c.up[6:8] + c.front[8:9])
        self.set_down(c.down[:2] + c.back[6:7] + c.down[3:5] + c.back[3:4] + c.down[6:8] + c.back[0:1])
        self.set_front(c.front[:2] + c.down[2:3] + c.front[3:5] + c.down[5:6] + c.front[6:8] + c.down[8:9])
        self.set_back(c.up[8:9] + c.back[1:3] + c.up[5:6] + c.back[4:6] + c.up[2:3] + c.back[7:])
        self.rotate_side(Rot.CLOCKWISE, Side.RIGHT)
        print("r") if print_flag else 0

    def move_not_r(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:2] + c.back[6:7] + c.up[3:5] + c.back[3:4] + c.up[6:8] + c.back[0:1])
        self.set_down(c.down[:2] + c.front[2:3] + c.down[3:5] + c.front[5:6] + c.down[6:8] + c.front[8:9])
        self.set_front(c.front[:2] + c.up[2:3] + c.front[3:5] + c.up[5:6] + c.front[6:8] + c.up[8:9])
        self.set_back(c.down[8:9] + c.back[1:3] + c.down[5:6] + c.back[4:6] + c.down[2:3] + c.back[7:])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.RIGHT)
        print("r'") if print_flag else 0

    def move_r2(self, print_flag=False):
        self.move_r()
        self.move_r()
        print("r2") if print_flag else 0

    def move_f(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:6] + c.left[8:9] + c.left[5:6] + c.left[2:3])
        self.set_down(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.down[3:])
        self.set_left(c.left[:2] + c.down[0:1] + c.left[3:5] + c.down[1:2] + c.left[6:8] + c.down[2:3])
        self.set_right(c.up[6:7] + c.right[1:3] + c.up[7:8] + c.right[4:6] + c.up[8:9] + c.right[7:])
        self.rotate_side(Rot.CLOCKWISE, Side.FRONT)
        print("f") if print_flag else 0

    def move_not_f(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.up[:6] + c.right[0:1] + c.right[3:4] + c.right[6:7])
        self.set_down(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.down[3:])
        self.set_left(c.left[:2] + c.up[8:9] + c.left[3:5] + c.up[7:8] + c.left[6:8] + c.up[6:7])
        self.set_right(c.down[2:3] + c.right[1:3] + c.down[1:2] + c.right[4:6] + c.down[0:1] + c.right[7:])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.FRONT)
        print("f'") if print_flag else 0

    def move_f2(self, print_flag=False):
        self.move_f()
        self.move_f()
        print("f2") if print_flag else 0

    def move_b(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.up[3:])
        self.set_down(c.down[:6] + c.left[0:1] + c.left[3:4] + c.left[6:7])
        self.set_left(c.up[2:3] + c.left[1:3] + c.up[1:2] + c.left[4:6] + c.up[0:1] + c.left[7:])
        self.set_right(c.right[:2] + c.down[8:9] + c.right[3:5] + c.down[7:8] + c.right[6:8] + c.down[6:7])
        self.rotate_side(Rot.CLOCKWISE, Side.BACK)
        print("b") if print_flag else 0

    def move_not_b(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.up[3:])
        self.set_down(c.down[:6] + c.right[8:9] + c.right[5:6] + c.right[2:3])
        self.set_left(c.down[6:7] + c.left[1:3] + c.down[7:8] + c.left[4:6] + c.down[8:9] + c.left[7:])
        self.set_right(c.right[:2] + c.up[0:1] + c.right[3:5] + c.up[1:2] + c.right[6:8] + c.up[2:3])
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
        self.set_up(c.left[6:7] + c.left[3:4] + c.left[0:1] + c.left[7:8] + c.left[4:5]
                    + c.left[1:2] + c.left[8:9] + c.left[5:6] + c.left[2:3])
        self.set_down(c.right[6:7] + c.right[3:4] + c.right[0:1] + c.right[7:8] + c.right[4:5]
                      + c.right[1:2] + c.right[8:9] + c.right[5:6] + c.right[2:3])
        self.set_left(c.down[6:7] + c.down[3:4] + c.down[0:1] + c.down[7:8] + c.down[4:5]
                      + c.down[1:2] + c.down[8:9] + c.down[5:6] + c.down[2:3])
        self.set_right(c.up[6:7] + c.up[3:4] + c.up[0:1] + c.up[7:8] +
                       c.up[4:5] + c.up[1:2] + c.up[8:9] + c.up[5:6] + c.up[2:3])
        self.rotate_side(Rot.CLOCKWISE, Side.FRONT)
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.BACK)
        print("z") if print_flag else 0

    def move_not_z(self, print_flag=False):
        c = Cube(self._pos)
        self.set_up(c.right[2:3] + c.right[5:6] + c.right[8:9] + c.right[1:2]
                    + c.right[4:5] + c.right[7:8] + c.right[0:1] + c.right[3:4] + c.right[6:7])
        self.set_down(c.left[2:3] + c.left[5:6] + c.left[8:9] + c.left[1:2]
                      + c.left[4:5] + c.left[7:8] + c.left[0:1] + c.left[3:4] + c.left[6:7])
        self.set_left(c.up[2:3] + c.up[5:6] + c.up[8:9] + c.up[1:2] + c.up[4:5] +
                      c.up[7:8] + c.up[0:1] + c.up[3:4] + c.up[6:7])
        self.set_right(c.down[2:3] + c.down[5:6] + c.down[8:9] + c.down[1:2]
                       + c.down[4:5] + c.down[7:8] + c.down[0:1] + c.down[3:4] + c.down[6:7])
        self.rotate_side(Rot.COUNTER_CLOCKWISE, Side.FRONT)
        self.rotate_side(Rot.CLOCKWISE, Side.BACK)
        print("z'") if print_flag else 0

    # ######################## COLOR MOVES ######################## #

    def move_white(self, print_flag=False):
        if self._white_face == Side.UP:
            self.move_u()
        elif self._white_face == Side.DOWN:
            self.move_d()
        elif self._white_face == Side.LEFT:
            self.move_l()
        elif self._white_face == Side.RIGHT:
            self.move_r()
        elif self._white_face == Side.FRONT:
            self.move_f()
        elif self._white_face == Side.BACK:
            self.move_b()
        else:
            print("ERROR #7")

    def move_not_white(self, print_flag=False):
        if self._white_face == Side.UP:
            self.move_not_u()
        elif self._white_face == Side.DOWN:
            self.move_not_d()
        elif self._white_face == Side.LEFT:
            self.move_not_l()
        elif self._white_face == Side.RIGHT:
            self.move_not_r()
        elif self._white_face == Side.FRONT:
            self.move_not_f()
        elif self._white_face == Side.BACK:
            self.move_not_b()
        else:
            print("ERROR #8")

    def move_white2(self, print_flag=False):
        if self._white_face == Side.UP:
            self.move_u2()
        elif self._white_face == Side.DOWN:
            self.move_d2()
        elif self._white_face == Side.LEFT:
            self.move_l2()
        elif self._white_face == Side.RIGHT:
            self.move_r2()
        elif self._white_face == Side.FRONT:
            self.move_f2()
        elif self._white_face == Side.BACK:
            self.move_b2()
        else:
            print("ERROR #9")

    def move_yellow(self, print_flag=False):
        if self._yellow_face == Side.UP:
            self.move_u()
        elif self._yellow_face == Side.DOWN:
            self.move_d()
        elif self._yellow_face == Side.LEFT:
            self.move_l()
        elif self._yellow_face == Side.RIGHT:
            self.move_r()
        elif self._yellow_face == Side.FRONT:
            self.move_f()
        elif self._yellow_face == Side.BACK:
            self.move_b()
        else:
            print("ERROR #10")

    def move_not_yellow(self, print_flag=False):
        if self._yellow_face == Side.UP:
            self.move_not_u()
        elif self._yellow_face == Side.DOWN:
            self.move_not_d()
        elif self._yellow_face == Side.LEFT:
            self.move_not_l()
        elif self._yellow_face == Side.RIGHT:
            self.move_not_r()
        elif self._yellow_face == Side.FRONT:
            self.move_not_f()
        elif self._yellow_face == Side.BACK:
            self.move_not_b()
        else:
            print("ERROR #11")

    def move_yellow2(self, print_flag=False):
        if self._yellow_face == Side.UP:
            self.move_u2()
        elif self._yellow_face == Side.DOWN:
            self.move_d2()
        elif self._yellow_face == Side.LEFT:
            self.move_l2()
        elif self._yellow_face == Side.RIGHT:
            self.move_r2()
        elif self._yellow_face == Side.FRONT:
            self.move_f2()
        elif self._yellow_face == Side.BACK:
            self.move_b2()
        else:
            print("ERROR #12")

    def move_green(self, print_flag=False):
        if self._green_face == Side.UP:
            self.move_u()
        elif self._green_face == Side.DOWN:
            self.move_d()
        elif self._green_face == Side.LEFT:
            self.move_l()
        elif self._green_face == Side.RIGHT:
            self.move_r()
        elif self._green_face == Side.FRONT:
            self.move_f()
        elif self._green_face == Side.BACK:
            self.move_b()
        else:
            print("ERROR #13")

    def move_not_green(self, print_flag=False):
        if self._green_face == Side.UP:
            self.move_not_u()
        elif self._green_face == Side.DOWN:
            self.move_not_d()
        elif self._green_face == Side.LEFT:
            self.move_not_l()
        elif self._green_face == Side.RIGHT:
            self.move_not_r()
        elif self._green_face == Side.FRONT:
            self.move_not_f()
        elif self._green_face == Side.BACK:
            self.move_not_b()
        else:
            print("ERROR #14")

    def move_green2(self, print_flag=False):
        if self._green_face == Side.UP:
            self.move_u2()
        elif self._green_face == Side.DOWN:
            self.move_d2()
        elif self._green_face == Side.LEFT:
            self.move_l2()
        elif self._green_face == Side.RIGHT:
            self.move_r2()
        elif self._green_face == Side.FRONT:
            self.move_f2()
        elif self._green_face == Side.BACK:
            self.move_b2()
        else:
            print("ERROR #15")

    def move_blue(self, print_flag=False):
        if self._blue_face == Side.UP:
            self.move_u()
        elif self._blue_face == Side.DOWN:
            self.move_d()
        elif self._blue_face == Side.LEFT:
            self.move_l()
        elif self._blue_face == Side.RIGHT:
            self.move_r()
        elif self._blue_face == Side.FRONT:
            self.move_f()
        elif self._blue_face == Side.BACK:
            self.move_b()
        else:
            print("ERROR #16")

    def move_not_blue(self, print_flag=False):
        if self._blue_face == Side.UP:
            self.move_not_u()
        elif self._blue_face == Side.DOWN:
            self.move_not_d()
        elif self._blue_face == Side.LEFT:
            self.move_not_l()
        elif self._blue_face == Side.RIGHT:
            self.move_not_r()
        elif self._blue_face == Side.FRONT:
            self.move_not_f()
        elif self._blue_face == Side.BACK:
            self.move_not_b()
        else:
            print("ERROR #17")

    def move_blue2(self, print_flag=False):
        if self._blue_face == Side.UP:
            self.move_u2()
        elif self._blue_face == Side.DOWN:
            self.move_d2()
        elif self._blue_face == Side.LEFT:
            self.move_l2()
        elif self._blue_face == Side.RIGHT:
            self.move_r2()
        elif self._blue_face == Side.FRONT:
            self.move_f2()
        elif self._blue_face == Side.BACK:
            self.move_b2()
        else:
            print("ERROR #18")

    def move_red(self, print_flag=False):
        if self._red_face == Side.UP:
            self.move_u()
        elif self._red_face == Side.DOWN:
            self.move_d()
        elif self._red_face == Side.LEFT:
            self.move_l()
        elif self._red_face == Side.RIGHT:
            self.move_r()
        elif self._red_face == Side.FRONT:
            self.move_f()
        elif self._red_face == Side.BACK:
            self.move_b()
        else:
            print("ERROR #19")

    def move_not_red(self, print_flag=False):
        if self._red_face == Side.UP:
            self.move_not_u()
        elif self._red_face == Side.DOWN:
            self.move_not_d()
        elif self._red_face == Side.LEFT:
            self.move_not_l()
        elif self._red_face == Side.RIGHT:
            self.move_not_r()
        elif self._red_face == Side.FRONT:
            self.move_not_f()
        elif self._red_face == Side.BACK:
            self.move_not_b()
        else:
            print("ERROR #20")

    def move_red2(self, print_flag=False):
        if self._red_face == Side.UP:
            self.move_u2()
        elif self._red_face == Side.DOWN:
            self.move_d2()
        elif self._red_face == Side.LEFT:
            self.move_l2()
        elif self._red_face == Side.RIGHT:
            self.move_r2()
        elif self._red_face == Side.FRONT:
            self.move_f2()
        elif self._red_face == Side.BACK:
            self.move_b2()
        else:
            print("ERROR #21")

    def move_orange(self, print_flag=False):
        if self._orange_face == Side.UP:
            self.move_u()
        elif self._orange_face == Side.DOWN:
            self.move_d()
        elif self._orange_face == Side.LEFT:
            self.move_l()
        elif self._orange_face == Side.RIGHT:
            self.move_r()
        elif self._orange_face == Side.FRONT:
            self.move_f()
        elif self._orange_face == Side.BACK:
            self.move_b()
        else:
            print("ERROR #22")

    def move_not_orange(self, print_flag=False):
        if self._orange_face == Side.UP:
            self.move_not_u()
        elif self._orange_face == Side.DOWN:
            self.move_not_d()
        elif self._orange_face == Side.LEFT:
            self.move_not_l()
        elif self._orange_face == Side.RIGHT:
            self.move_not_r()
        elif self._orange_face == Side.FRONT:
            self.move_not_f()
        elif self._orange_face == Side.BACK:
            self.move_not_b()
        else:
            print("ERROR #23")

    def move_orange2(self, print_flag=False):
        if self._orange_face == Side.UP:
            self.move_u2()
        elif self._orange_face == Side.DOWN:
            self.move_d2()
        elif self._orange_face == Side.LEFT:
            self.move_l2()
        elif self._orange_face == Side.RIGHT:
            self.move_r2()
        elif self._orange_face == Side.FRONT:
            self.move_f2()
        elif self._orange_face == Side.BACK:
            self.move_b2()
        else:
            print("ERROR #24")

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
            # print(self)
            # print("\n-----------------------")

    def randomize(self):
        number_of_moves = random.randint(10, 20)
        for n in range(number_of_moves):
            self.move(random.choice(Cube.MOVES))

    def solve(self):
        # return solve chain
        pass


def main():
    rubiks_cube = Cube(Cube.SOLVED_POS)
    print(rubiks_cube)

    rubiks_cube.follow_move_chain(Cube.MOVES3)
    rubiks_cube.move_y()
    rubiks_cube.move_y()
    rubiks_cube.follow_move_chain(Cube.MOVES3)
    rubiks_cube.move_y()
    rubiks_cube.move_y()
    rubiks_cube.follow_move_chain(Cube.MOVES4)

    print(rubiks_cube)
    print("\n")

    # print(Cube.MOVES2)
    #

if __name__ == '__main__':
    main()
