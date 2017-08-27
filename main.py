#!/usr/bin/env python3

from time import sleep
from sys import stdout
from os import get_terminal_size
from cube_class import Color, Cube
import ev3dev.ev3 as ev3
from ev3dev.ev3 import Sound
from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor


class Robot:
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

    def __init__(self):
        self.cradle = LargeMotor(OUTPUT_A)
        self.swing_arm = LargeMotor(OUTPUT_B)
        self.cs_arm = MediumMotor(OUTPUT_C)

        self.ts = ev3.TouchSensor()
        self.cs = ColorSensor()
        self.cs.mode = self.cs.MODE_COL_COLOR

        self.cs_mid_pos = -1700
        self.cs_cor_pos = -1390
        self.cs_cen_pos = -2500
        self.cube_rot_speed = 100
        self.cs_speed = 1000
        self.swing_arm_speed = 200
        self._scanned_cubies = 0

    def init_motors(self):
        self.cradle.stop_action = "coast"
        self.cradle.run_timed(time_sp=1, speed_sp=1)
        self.swing_arm.stop_action = "coast"
        self.swing_arm.run_timed(time_sp=1, speed_sp=1)
        self.cs_arm.stop_action = "coast"
        self.cs_arm.run_timed(time_sp=1, speed_sp=1)

        while self.ts.value() != 1:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)

        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        self.cradle.stop_action = "hold"
        self.swing_arm.stop_action = "hold"
        self.cs_arm.stop_action = "hold"

        self.cradle.position = 0
        self.swing_arm.position = 0
        self.cs_arm.position = 0

        Sound.beep()

    def rotate_cradle(self, angle, guarded=False):
        if guarded:
            print("g")
            if angle > 0:
                guard_over_rotation = 20
                guard_return = 21
            else:
                guard_over_rotation = -20
                guard_return = -21

            new_pos = self.cradle.position + angle + guard_over_rotation
            self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed, ramp_down_sp=50)
            self.cradle.wait_for_position(new_pos)
            new_pos = self.cradle.position - guard_return
            self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed, ramp_down_sp=50)
            self.cradle.wait_for_position(new_pos)
        else:
            new_pos = self.cradle.position + angle
            self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed, ramp_down_sp=50)
            self.cradle.wait_for_position(new_pos)

    def hold(self, message):
        print("\nHolding: '" + message + "'\n")
        Sound.tone([(800, 150, 0), (400, 150, 0), (800, 150, 0), (400, 150, 0)]).wait()
        while self.ts.value() != 1:
            pass

    def increment_progressbar(self):
        # Progressbar will change width depending on console size
        dims = get_terminal_size()

        if dims[0] > 64:
            progressbar_width = 54
        else:
            progressbar_width = dims[0] - 10

        # Increment number of scanned cubies, and scale it for sizing
        self._scanned_cubies += 1
        progress = int(self._scanned_cubies/(54/progressbar_width))

        stdout.write("\r|")
        stdout.write("#" * progress)
        stdout.write("-" * (progressbar_width - progress))
        stdout.write("| %.2f%%" % ((self._scanned_cubies/54)*100))
        stdout.flush()

    def scan_up_face(self):
        middle = []
        corner = []

        for i in range(4):
            # Middle
            self.cs_arm.run_to_abs_pos(position_sp=self.cs_mid_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_mid_pos)
            middle.append(Color(self.cs.value()))

            self.increment_progressbar()

            # Corner
            self.rotate_cradle(-45)
            # new_pos = self.cradle.position - 45
            # self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed)
            # self.cradle.wait_for_position(new_pos)

            self.cs_arm.run_to_abs_pos(position_sp=self.cs_cor_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_cor_pos)
            corner.append(Color(self.cs.value()))

            self.increment_progressbar()

            # Prep for next middle
            self.rotate_cradle(-45)
            # new_pos = self.cradle.position - 45
            # self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed)
            # self.cradle.wait_for_position(new_pos)

        # Read centre cubie
        self.cs_arm.run_to_abs_pos(position_sp=self.cs_cen_pos, speed_sp=self.cs_speed)
        self.cs_arm.wait_for_position(self.cs_cen_pos)
        centre = Color(self.cs.value())

        self.increment_progressbar()

        """
        The face is scanned in this order:
            1 1 0
            2 C 0
            2 3 3
        """

        return corner[1], middle[1], corner[0], middle[2], centre, middle[0], corner[2], middle[3], corner[3]

    def scan_cube(self, simulate=False):
        # - Z Z Z Y Z Z Z
        # U L D R - F - B    <---- Initial State
        # B R F L - D - U    <---- Final State!!

        print("Scanning Rubik's Cube...")

        sides = [[], [], [], [], [], []]

        # Move swing arm out of the way
        self.swing_arm.run_to_abs_pos(position_sp=60, speed_sp=self.swing_arm_speed)
        self.swing_arm.wait_for_position(60)

        if not simulate:
            for i in range(len(sides)):
                sides[i] = self.scan_up_face()

                self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
                self.cs_arm.wait_for_position(0)

                if i == 3:
                    new_pos = self.cradle.position - 90
                    self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed)
                    self.cradle.wait_for_position(new_pos)

                if i < 5:
                    new_pos = self.swing_arm.position - 360
                    self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=self.swing_arm_speed)
                    self.swing_arm.wait_for_position(new_pos)

                if i == 4:
                    new_pos = self.swing_arm.position - 360
                    self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=self.swing_arm_speed)
                    self.swing_arm.wait_for_position(new_pos)

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
        else:
            for i in range(54):
                sleep(0.005)
                self.increment_progressbar()

            sides = [(Color.BLUE, Color.WHITE, Color.ORANGE, Color.RED,
                      Color.WHITE, Color.ORANGE, Color.GREEN, Color.WHITE, Color.GREEN),
                     (Color.ORANGE, Color.YELLOW, Color.RED, Color.BLUE,
                      Color.RED, Color.GREEN, Color.WHITE, Color.WHITE, Color.ORANGE),
                     (Color.YELLOW, Color.YELLOW, Color.BLUE, Color.YELLOW,
                      Color.YELLOW, Color.RED, Color.BLUE, Color.ORANGE, Color.GREEN),
                     (Color.BLUE, Color.WHITE, Color.GREEN, Color.BLUE,
                      Color.ORANGE, Color.GREEN, Color.ORANGE, Color.YELLOW, Color.RED),
                     (Color.YELLOW, Color.GREEN, Color.RED, Color.BLUE,
                      Color.BLUE, Color.ORANGE, Color.WHITE, Color.BLUE, Color.YELLOW),
                     (Color.YELLOW, Color.GREEN, Color.WHITE, Color.RED,
                      Color.GREEN, Color.ORANGE, Color.RED, Color.RED, Color.WHITE)]

        # rotate DOWN 180deg to account for physical transformations
        sides[4] = sides[4][::-1]

        cube_pos = []
        for side in sides:
            for i in side:
                cube_pos.append(i)

        corrected_cube_pos = cube_pos[45:] +\
            cube_pos[27:30] + cube_pos[18:21] + cube_pos[9:12] + cube_pos[:3] + \
            cube_pos[30:33] + cube_pos[21:24] + cube_pos[12:15] + cube_pos[3:6] + \
            cube_pos[33:36] + cube_pos[24:27] + cube_pos[15:18] + cube_pos[6:9] + \
            cube_pos[36:45]

        print()
        return corrected_cube_pos

    def exit(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=1000)
        self.cs_arm.wait_for_position(0)
        # self.cradle.run_to_abs_pos(position_sp=0, speed_sp=500)
        # self.cradle.wait_for_position(0)
        self.swing_arm.run_to_abs_pos(position_sp=0, speed_sp=1020, ramp_down_sp=500)
        self.swing_arm.wait_for_position(0)

        sleep(1)

        self.cradle.stop_action = "coast"
        self.cradle.run_timed(time_sp=1, speed_sp=1)
        self.swing_arm.stop_action = "coast"
        self.swing_arm.run_timed(time_sp=1, speed_sp=1)
        self.cs_arm.stop_action = "coast"
        self.cs_arm.run_timed(time_sp=1, speed_sp=1)
        print("\n\n")
        Sound.tone([(800, 100, 0), (600, 150, 0), (400, 100, 0)]).wait()

    def robotify_moves(self, move_chain):
        # Turn secondary/tertiary moves into primary moves
        pass

    def move_d(self):
        # print("SA: " + str(self.swing_arm.position))
        # Set guards to block position
        if not( 5 <= (self.swing_arm.position-60) % 360 <= 355):
            guard_pos = self.swing_arm.position - 60
            self.swing_arm.run_to_abs_pos(position_sp=guard_pos, speed_sp=self.swing_arm_speed)
            self.swing_arm.wait_for_position(guard_pos)

        # Rotate Cradle +90
        self.rotate_cradle(90, True)

    def move_not_d(self):
        # Set guards to block position
        if not( 5 <= (self.swing_arm.position-60) % 360 <= 355):
            guard_pos = self.swing_arm.position - 60
            self.swing_arm.run_to_abs_pos(position_sp=guard_pos, speed_sp=self.swing_arm_speed)
            self.swing_arm.wait_for_position(guard_pos)

        # Rotate Cradle -90
        self.rotate_cradle(-90, True)

    def move_y(self):
        # Remove guards
        if not( 5 <= self.swing_arm.position % 360 <= 355):
            guard_pos = self.swing_arm.position + 60
            self.swing_arm.run_to_abs_pos(position_sp=guard_pos, speed_sp=self.swing_arm_speed)
            self.swing_arm.wait_for_position(guard_pos)

        # Rotate Cradle +90
        self.rotate_cradle(90)

    def move_not_y(self):
        # Remove guards
        if not( 5 <= self.swing_arm.position % 360 <= 355):
            guard_pos = self.swing_arm.position + 60
            self.swing_arm.run_to_abs_pos(position_sp=guard_pos, speed_sp=self.swing_arm_speed)
            self.swing_arm.wait_for_position(guard_pos)

        # Rotate Cradle -90
        self.rotate_cradle(-90)
        pass

    def move_z(self):
        # Rotate swing arm 360
        new_pos = self.swing_arm.position - 360
        self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=self.swing_arm_speed)
        self.swing_arm.wait_for_position(new_pos)

    def run_move_chain(self, move_chain):
        # Check move_chain is 'robotified'
        # Run move_chain
        pass

    def move_tester(self):
        move_num = ''
        while move_num != '0':
            move_num = input("1: D   2: ~D   3: Y   4:~Y   5: Z   ?: ")
            print(move_num)
            if move_num == '1':
                print("move_d")
                self.move_d()
            elif move_num == '2':
                print("move_not_d")
                self.move_not_d()
            elif move_num == '3':
                print("move_y")
                self.move_y()
            elif move_num == '4':
                print("move_not_y")
                self.move_not_y()
            elif move_num == '5':
                print("move_z")
                self.move_z()


def main():
    simulate_bot = True

    Sound.beep()
    rubiks_bot = Robot()
    try:
        rubiks_bot.init_motors()
        rubiks_cube = Cube(rubiks_bot.scan_cube(simulate_bot))
        print(rubiks_cube)

        rubiks_bot.move_tester()
        # rubiks_bot.move_d()
        # Sound.beep()
        # rubiks_bot.move_not_d()
        # Sound.beep()
        # rubiks_bot.move_not_d()
        # Sound.beep()

        solve_chain = rubiks_cube.solve
        robot_moves = rubiks_bot.robotify_moves(solve_chain)
        rubiks_bot.run_move_chain(robot_moves)
    except KeyboardInterrupt:
        pass  # Stops immediate sys.exit to run custom exit function
    except TypeError as e:
        print("TypeError: " + str(e))
    rubiks_bot.exit()

if __name__ == "__main__":
    main()
