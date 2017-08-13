from enum import Enum


class Side(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    FRONT = 4
    BACK = 5

class Dir(Enum):
    CLOCKWISE = 0
    COUNTER_CLOCKWISE = 1

class Cube:
    """A Rubik's Cube with 54 different coloured tiles"""

    # Default cube position as a net, written as rows from up to down
    SOLVED_POS = "WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY"
    DEBUG_POS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12"
    MOVES = ["R", "NotR", "L", "NotL", "R2", "L2", "U", "NotU", "D", "NotD", "U2", "D2",
             "F", "NotF", "B", "NotB", "F2", "B2", "M", "NotM", "M2", "E", "NotE", "E2", "S", "NotS", "S2",
             "X", "NotX", "Y", "NotY", "Z", "NotZ"]

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
        cube_net = "\n   " + self._pos[:3] + "\n   " + self._pos[3:6] + "\n   " + self._pos[6:9] +\
                   "\n" + self._pos[9:21] + "\n" + self._pos[21:33] + "\n" + self._pos[33:45] +\
                   "\n   " + self._pos[45:48] + "\n   " + self._pos[48:51] + "\n   " + self._pos[51:54]

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

        if direction == Dir.CLOCKWISE:
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
        elif direction == Dir.COUNTER_CLOCKWISE:

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
    
    def move_l(self):
        c = Cube(self._pos)
        self.set_up(c.back[8] + c.up[1:3] + c.back[5] + c.up[4:6] + c.back[2] + c.up[7:])
        self.set_down(c.front[0] + c.down[1:3] + c.front[3] + c.down[4:6] + c.front[6] + c.down[7:])
        self.set_front(c.up[0] + c.front[1:3] + c.up[3] + c.front[4:6] + c.up[6] + c.front[7:])
        self.set_back(c.back[0:2] + c.down[6] + c.back[3:5] + c.down[3] + c.back[6:8] + c.down[0])
        self.rotate_side(Dir.CLOCKWISE, Side.LEFT)

    def move_not_l(self):
        c = Cube(self._pos)
        self.set_up(c.front[0] + c.up[1:3] + c.front[3] + c.up[4:6] + c.front[6] + c.up[7:])
        self.set_down(c.back[8] + c.down[1:3] + c.back[5] + c.down[4:6] + c.back[2] + c.down[7:])
        self.set_front(c.down[0] + c.front[1:3] + c.down[3] + c.front[4:6] + c.down[6] + c.front[7:])
        self.set_back(c.back[0:2] + c.up[6] + c.back[3:5] + c.up[3] + c.back[6:8] + c.up[0])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.LEFT)

    def move_l2(self):
        self.move_l()
        self.move_l()
        
    def move_r(self):
        c = Cube(self._pos)
        self.set_up(c.up[:2] + c.front[2] + c.up[3:5] + c.front[5] + c.up[6:8] + c.front[8])
        self.set_down(c.down[:2] + c.back[6] + c.down[3:5] + c.back[3] + c.down[6:8] + c.back[0])
        self.set_front(c.front[:2] + c.down[2] + c.front[3:5] + c.down[5] + c.front[6:8] + c.down[8])
        self.set_back(c.up[8] + c.back[0:2] + c.up[5] + c.back[3:5] + c.up[2] + c.back[6:8])
        self.rotate_side(Dir.CLOCKWISE, Side.RIGHT)

    def move_not_r(self):
        c = Cube(self._pos)
        self.set_up(c.up[:2] + c.back[6] + c.up[3:5] + c.back[3] + c.up[6:8] + c.back[0])
        self.set_down(c.down[:2] + c.front[2] + c.down[3:5] + c.front[5] + c.down[6:8] + c.front[8])
        self.set_front(c.front[:2] + c.up[2] + c.front[3:5] + c.up[5] + c.front[6:8] + c.up[8])
        self.set_back(c.down[8] + c.back[1:3] + c.down[5] + c.back[4:6] + c.down[2] + c.back[7:])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.RIGHT)

    def move_r2(self):
        self.move_r()
        self.move_r()

    def move_u(self):
        c = Cube(self._pos)
        self.set_left(c.front[:3] + c.left[3:])
        self.set_right(c.back[:3] + c.right[3:])
        self.set_front(c.right[:3] + c.front[3:])
        self.set_back(c.left[:3] + c.back[3:])
        self.rotate_side(Dir.CLOCKWISE, Side.UP)

    def move_not_u(self):
        c = Cube(self._pos)
        self.set_left(c.back[:3] + c.left[3:])
        self.set_right(c.front[:3] + c.right[3:])
        self.set_front(c.left[:3] + c.front[3:])
        self.set_back(c.right[:3] + c.back[3:])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.UP)

    def move_u2(self):
        self.move_u()
        self.move_u()

    def move_d(self):
        c = Cube(self._pos)
        self.set_left(c.left[:6] + c.back[6:])
        self.set_right(c.right[:6] + c.front[6:])
        self.set_front(c.front[:6] + c.left[6:])
        self.set_back(c.back[:6] + c.right[6:])
        self.rotate_side(Dir.CLOCKWISE, Side.DOWN)

    def move_not_d(self):
        c = Cube(self._pos)
        self.set_left(c.left[:6] + c.front[6:])
        self.set_right(c.right[:6] + c.back[6:])
        self.set_front(c.front[:6] + c.right[6:])
        self.set_back(c.back[:6] + c.left[6:])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.DOWN)

    def move_d2(self):
        self.move_d()
        self.move_d()

    def move_f(self):
        c = Cube(self._pos)
        self.set_up(c.up[:6] + c.left[8] + c.left[5] + c.left[2])
        self.set_down(c.right[6] + c.right[3] + c.right[0] + c.down[3:])
        self.set_left(c.left[:1] + c.down[0] + c.left[3:5] + c.down[1] + c.left[6:7] + c.down[2])
        self.set_right(c.up[6] + c.right[1:3] + c.up[7] + c.right[4:6] + c.up[8] + c.right[7:])
        self.rotate_side(Dir.CLOCKWISE, Side.FRONT)

    def move_not_f(self):
        c = Cube(self._pos)
        self.set_up(c.up[:6] + c.right[0] + c.right[3] + c.right[6])
        self.set_down(c.left[2] + c.left[5] + c.left[8] + c.down[3:])
        self.set_left(c.left[:1] + c.up[8] + c.left[3:5] + c.up[7] + c.left[6:7] + c.up[6])
        self.set_right(c.down[2] + c.right[1:3] + c.down[1] + c.right[4:6] + c.down[0] + c.right[7:])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.FRONT)

    def move_f2(self):
        self.move_f()
        self.move_f()

    def move_b(self):
        c = Cube(self._pos)
        self.set_up(c.right[2] + c.right[5] + c.right[8] + c.up[3:])
        self.set_down(c.down[:5] + c.left[0] + c.left[3] + c.left[6])
        self.set_left(c.up[2] + c.left[1:3] + c.up[1] + c.left[4:6] + c.up[0] + c.left[7:])
        self.set_right(c.right[:2] + c.down[8] + c.right[3:5] + c.down[7] + c.right[6:8] + c.down[6])
        self.rotate_side(Dir.CLOCKWISE, Side.BACK)

    def move_not_b(self):
        c = Cube(self._pos)
        self.set_up(c.left[6] + c.left[3] + c.left[0] + c.up[3:])
        self.set_down(c.down[:5] + c.right[8] + c.right[5] + c.right[2])
        self.set_left(c.down[6] + c.left[1:3] + c.down[7] + c.left[4:6] + c.down[8] + c.left[7:])
        self.set_right(c.right[:2] + c.up[0] + c.right[3:5] + c.up[1] + c.right[6:8] + c.up[2])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.BACK)

    def move_b2(self):
        self.move_b()
        self.move_b()

    def move_m(self):
        self.move_r()
        self.move_not_l()
        self.move_not_x()

    def move_not_m(self):
        self.move_not_r()
        self.move_l()
        self.move_x()

    def move_m2(self):
        self.move_m()
        self.move_m()

    def move_e(self):
        self.move_u()
        self.move_not_d()
        self.move_not_y()

    def move_not_e(self):
        self.move_not_u()
        self.move_d()
        self.move_y()

    def move_e2(self):
        self.move_e()
        self.move_e()

    def move_s(self):
        self.move_not_f()
        self.move_b()
        self.move_z()

    def move_not_s(self):
        self.move_f()
        self.move_not_b()
        self.move_not_z()

    def move_s2(self):
        self.move_s()
        self.move_s()

    def move_x(self):
        c = Cube(self._pos)
        self.set_up(c.front)
        self.set_down(c.back[::-1])  # [::-1] reverses the string
        self.set_front(c.down)
        self.set_back(c.up[::-1])  # [::-1] reverses the string
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.LEFT)
        self.rotate_side(Dir.CLOCKWISE, Side.RIGHT)

    def move_not_x(self):
        c = Cube(self._pos)
        self.set_up(c.back[::-1])  # [::-1] reverses the string
        self.set_down(c.front)
        self.set_front(c.up)
        self.set_back(c.down[::-1])  # [::-1] reverses the string
        self.rotate_side(Dir.CLOCKWISE, Side.LEFT)
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.RIGHT)

    def move_y(self):
        c = Cube(self._pos)
        self.set_left(c.front)
        self.set_right(c.back)
        self.set_front(c.right)
        self.set_back(c.left)
        self.rotate_side(Dir.CLOCKWISE, Side.UP)
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.DOWN)

    def move_not_y(self):
        c = Cube(self._pos)
        self.set_left(c.back)
        self.set_right(c.front)
        self.set_front(c.left)
        self.set_back(c.right)
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.UP)
        self.rotate_side(Dir.CLOCKWISE, Side.DOWN)

    def move_z(self):
        c = Cube(self._pos)
        self.set_up(c.left[6] + c.left[3] + c.left[0] + c.left[7] + c.left[4] + c.left[1] + c.left[8] + c.left[5] + c.left[2])
        self.set_down(c.right[6] + c.right[3] + c.right[0] + c.right[7] + c.right[4] + c.right[1] + c.right[8] + c.right[5] + c.right[2])
        self.set_left(c.down[6] + c.down[3] + c.down[0] + c.down[7] + c.down[4] + c.down[1] + c.down[8] + c.down[5] + c.down[2])
        self.set_right(c.up[6] + c.up[3] + c.up[0] + c.up[7] + c.up[4] + c.up[1] + c.up[8] + c.up[5] + c.up[2])
        self.rotate_side(Dir.CLOCKWISE, Side.FRONT)
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.BACK)
*
    def move_not_z(self):
        c = Cube(self._pos)
        self.set_up(c.right[2] + c.right[5] + c.right[8] + c.right[1] + c.right[4] + c.right[7] + c.right[0] + c.right[3] + c.right[6])
        self.set_down(c.left[2] + c.left[5] + c.left[8] + c.left[1] + c.left[4] + c.left[7] + c.left[0] + c.left[3] + c.left[6])
        self.set_left(c.up[2] + c.up[5] + c.up[8] + c.up[1] + c.up[4] + c.up[7] + c.up[0] + c.up[3] + c.up[6])
        self.set_right(c.down[2] + c.down[5] + c.down[8] + c.down[1] + c.down[4] + c.down[7] + c.down[0] + c.down[3] + c.down[6])
        self.rotate_side(Dir.COUNTER_CLOCKWISE, Side.FRONT)
        self.rotate_side(Dir.CLOCKWISE, Side.BACK)

def main():
    # rubiks_cube = Cube(Cube.SOLVED_POS)
    rubiks_cube = Cube(Cube.DEBUG_POS)
    print(rubiks_cube)
    # rubiks_cube.set_up("abcdefghi")
    # print(rubiks_cube)
    # rubiks_cube.move_u()
    # print(rubiks_cube)
    # rubiks_cube.move_not_u()
    # print(rubiks_cube)
    # rubiks_cube.rotate_side_cw(Side.UP)
    # rubiks_cube.rotate_side_cw(Side.UP)
    # rubiks_cube.rotate_side_cw(Side.UP)
    # rubiks_cube.rotate_side_cw(Side.UP)
    # rubiks_cube.rotate_side_ccw(Side.UP)
    # print(rubiks_cube)


if __name__ == '__main__':
    main()
