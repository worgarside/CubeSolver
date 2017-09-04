import data
from time import sleep
from sys import stdout
from os import get_terminal_size
from color_class import Color
import ev3dev.ev3 as ev3
from ev3dev.ev3 import Sound
from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor


class Robot:
    def __init__(self):
        self.cradle = LargeMotor(OUTPUT_A)
        self.grabber = LargeMotor(OUTPUT_B)
        self.cs_arm = MediumMotor(OUTPUT_C)
        self.ts = ev3.TouchSensor()
        self.cs = ColorSensor()
        self.cs.mode = self.cs.MODE_COL_COLOR

        self.cs_mid_pos = -1700
        self.cs_cor_pos = -1390
        self.cs_cen_pos = -2500
        self.cradle_speed = 1020
        self.cs_speed = 1020
        self.grabber_speed = 380
        self._scanned_cubies = 0

        self.gbr_no_guard_pos = 65
        self.gbr_guard_pos = -35
        self.gbr_grab_pos = -90

    def init_motors(self, simulate=False):
        if not simulate:
            self.cradle.stop_action = "coast"
            self.cradle.run_timed(time_sp=1, speed_sp=1)
            self.grabber.stop_action = "coast"
            self.grabber.run_timed(time_sp=1, speed_sp=1)
            self.cs_arm.stop_action = "coast"
            self.cs_arm.run_timed(time_sp=1, speed_sp=1)

            while self.ts.value() != 1:
                ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
                ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)

            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        self.cradle.stop_action = "hold"
        self.grabber.stop_action = "hold"
        self.cs_arm.stop_action = "hold"

        self.cradle.position = 0
        self.grabber.position = 0
        self.cs_arm.position = 0

        Sound.beep()

    def exit(self, stall_flag=False):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        if not stall_flag:
            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(0)
            # self.cradle.run_to_abs_pos(position_sp=0, speed_sp=self.cradle_speed)
            # self.cradle.wait_for_position(0)
            self.grabber.run_to_abs_pos(position_sp=0, speed_sp=self.grabber_speed, ramp_down_sp=50)
            self.grabber.wait_for_position(0)

        sleep(1)

        self.cradle.stop_action = "coast"
        self.cradle.run_timed(time_sp=1, speed_sp=1)
        self.grabber.stop_action = "coast"
        self.grabber.run_timed(time_sp=1, speed_sp=1)
        self.cs_arm.stop_action = "coast"
        self.cs_arm.run_timed(time_sp=1, speed_sp=1)
        print()
        print()
        Sound.tone([(800, 100, 0), (600, 150, 0), (400, 100, 0)]).wait()
        exit()

    def rotate_cradle(self, angle=90):
        # 1200 is 1/4 turn - 40/3:1 gear ratio
        mod_angle = angle * (40 / 3)
        pos = self.cradle.position + mod_angle
        self.cradle.run_to_abs_pos(position_sp=pos, speed_sp=self.cradle_speed, ramp_down_sp=100)
        self.cradle.wait_for_position(pos)

    def grab_cube(self, iters=1):
        for x in range(iters):
            self.grabber.run_to_abs_pos(position_sp=self.gbr_grab_pos, speed_sp=self.grabber_speed)
            self.grabber.wait_for_position(self.gbr_grab_pos)

            self.grabber.run_to_abs_pos(position_sp=-10, speed_sp=self.grabber_speed)
            self.grabber.wait_for_position(-10)

            self.grabber.run_to_abs_pos(position_sp=self.gbr_guard_pos, speed_sp=self.grabber_speed)
            self.grabber.wait_for_position(self.gbr_guard_pos)

    def increment_progressbar(self):
        # Progressbar will change width depending on console size
        dims = get_terminal_size()

        if dims[0] > 64:
            progressbar_width = 54
        else:
            progressbar_width = dims[0] - 10

        # Increment number of scanned cubies, and scale it for sizing
        self._scanned_cubies += 1
        progress = int(self._scanned_cubies / (54 / progressbar_width))

        stdout.write("\r|")
        stdout.write("#" * progress)
        stdout.write("-" * (progressbar_width - progress))
        stdout.write("| %.2f%%" % ((self._scanned_cubies / 54) * 100))
        stdout.flush()

    def scan_up_face(self):
        middle = []
        corner = []

        self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_no_guard_pos)

        for i in range(4):
            # Middle
            self.cs_arm.run_to_abs_pos(position_sp=self.cs_mid_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_mid_pos)
            middle.append(Color(self.cs.value()))

            self.increment_progressbar()

            # Corner
            self.rotate_cradle(45)

            self.cs_arm.run_to_abs_pos(position_sp=self.cs_cor_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_cor_pos)
            corner.append(Color(self.cs.value()))

            self.increment_progressbar()

            # Prep for next middle
            self.rotate_cradle(45)

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
        # - X X X Y X X X
        # U F D B - R - L    <---- Initial State
        # L B R F - D - U   <---- Final State!!

        print("Scanning Rubik's Cube...")

        sides = [[], [], [], [], [], []]

        # Move swing arm out of the way
        self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed / 2)
        self.grabber.wait_for_position(self.gbr_no_guard_pos)

        if not simulate:
            for i in range(len(sides)):
                sides[i] = self.scan_up_face()

                self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
                self.cs_arm.wait_for_position(0)

                if i == 3:
                    self.rotate_cradle(90)

                if i < 5:
                    self.grab_cube()

                if i == 4:
                    self.grab_cube()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
        else:
            for i in range(54):
                sleep(0.005)
                self.increment_progressbar()

            sides = data.SOLVED_SIDES

        sides[0] = sides[0][6:7] + sides[0][3:4] + sides[0][0:1] + sides[0][7:8] + sides[0][4:5] + sides[0][1:2] + \
            sides[0][8:9] + sides[0][5:6] + sides[0][2:3]

        sides[1] = sides[1][6:7] + sides[1][3:4] + sides[1][0:1] + sides[1][7:8] + sides[1][4:5] + sides[1][1:2] + \
            sides[1][8:9] + sides[1][5:6] + sides[1][2:3]

        sides[2] = sides[2][6:7] + sides[2][3:4] + sides[2][0:1] + sides[2][7:8] + sides[2][4:5] + sides[2][1:2] + \
            sides[2][8:9] + sides[2][5:6] + sides[2][2:3]

        sides[3] = sides[3][6:7] + sides[3][3:4] + sides[3][0:1] + sides[3][7:8] + sides[3][4:5] + sides[3][1:2] + \
            sides[3][8:9] + sides[3][5:6] + sides[3][2:3]

        cube_pos = []
        for side in sides:
            for i in side:
                cube_pos.append(i)

        corrected_cube_pos = cube_pos[45:] + \
            cube_pos[0:3] + cube_pos[27:30] + cube_pos[18:21] + cube_pos[9:12] + \
            cube_pos[3:6] + cube_pos[30:33] + cube_pos[21:24] + cube_pos[12:15] + \
            cube_pos[6:9] + cube_pos[33:36] + cube_pos[24:27] + cube_pos[15:18] + \
            cube_pos[36:45]

        return corrected_cube_pos

    def r_move_d(self):
        # Set guards to block position
        self.grabber.run_to_abs_pos(position_sp=self.gbr_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_guard_pos)

        # Rotate Cradle -90
        self.rotate_cradle(-96)
        self.rotate_cradle(6)

    def r_move_not_d(self):
        # Set guards to block position
        self.grabber.run_to_abs_pos(position_sp=self.gbr_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_guard_pos)

        # Rotate Cradle 90
        self.rotate_cradle(96)
        self.rotate_cradle(-6)

    def r_move_d2(self):
        # Set guards to block position
        self.r_move_d()
        self.r_move_d()

    def r_move_x(self):
        # Grab cube
        self.grab_cube()

    def r_move_x2(self):
        # Grab cube
        self.grab_cube()
        self.grab_cube()

    def r_move_y(self):
        # Remove guards
        self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_no_guard_pos)
        # Rotate Cradle +90
        self.rotate_cradle(90)

    def r_move_not_y(self):
        # Remove guards
        self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_no_guard_pos)
        # Rotate Cradle -90
        self.rotate_cradle(-90)

    def r_move_y2(self):
        # Remove guards
        self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_no_guard_pos)
        # Rotate Cradle +90
        self.rotate_cradle(180)

    def run_move_method(self, move):
        try:
            method = getattr(Robot, 'r_move_' + move)
            method(self)
        except AttributeError as e:
            print('rmove failed: \'' + move + '\' | ' + str(e))
            exit()

    def run_move_sequence(self, move_chain):
        # Check move_chain is 'robotified'
        for move in move_chain:
            self.run_move_method(move)
