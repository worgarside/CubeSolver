from os import get_terminal_size
from sys import stdout
from time import sleep

from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.ev3 import *
from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor

from cube.color_class import Color

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


class Robot:
    """A LEGO EV3 Robot with 3 motors, a colour sensor, and a touch sensor"""

    def __init__(self, simulation=False):
        self.peripherals = []
        self.simulated = simulation
        self.cradle = LargeMotor(OUTPUT_A)
        self.grabber = LargeMotor(OUTPUT_B)
        self.cs_arm = MediumMotor(OUTPUT_C)
        self.touch_sensor = TouchSensor()
        self.color_sensor = ColorSensor()

        self.peripherals.append(self.cradle)
        self.peripherals.append(self.grabber)
        self.peripherals.append(self.cs_arm)
        self.peripherals.append(self.touch_sensor)
        self.peripherals.append(self.color_sensor)

        self.color_sensor.mode = self.color_sensor.MODE_COL_COLOR
        self.color_scan_dict = {0: Color.NONE, 1: Color.DARK, 2: Color.BLUE, 3: Color.GREEN, 4: Color.YELLOW,
                                5: Color.RED, 6: Color.WHITE, 7: Color.ORANGE, }

        self.cs_mid_pos = -1650
        self.cs_cor_pos = -1350
        self.cs_cen_pos = -2300
        self.cradle_speed = 1020
        self.cs_speed = 1020
        self.grabber_speed = 325
        self._scanned_cubies = 0

        self.gbr_no_guard_pos = 65
        self.gbr_guard_pos = -35
        self.gbr_grab_pos = -90

        self.check_peripherals()

    def init_motors(self, override=False):
        """
        Allows user to manually position the motors at their starting position
        :param override: a flag to skip the initialisation for testing
        :return: None
        """

        if override:
            simulate_initialisation = False
        else:
            simulate_initialisation = self.simulated

        self.cradle.stop_action = 'coast'
        self.cradle.run_timed(time_sp=1, speed_sp=1)
        self.grabber.stop_action = 'coast'
        self.grabber.run_timed(time_sp=1, speed_sp=1)
        self.cs_arm.stop_action = 'coast'
        self.cs_arm.run_timed(time_sp=1, speed_sp=1)

        if not simulate_initialisation:
            wait_count = 0
            amber = True
            Sound.speak('initialise motors')
            while self.touch_sensor.value() != 1:
                wait_count += 1
                if wait_count % 50 == 0:
                    if amber:
                        Leds.set_color(Leds.LEFT, Leds.AMBER)
                        Leds.set_color(Leds.RIGHT, Leds.AMBER)
                    else:
                        Leds.set_color(Leds.LEFT, Leds.GREEN)
                        Leds.set_color(Leds.RIGHT, Leds.GREEN)
                    amber = not amber

            Leds.set_color(Leds.LEFT, Leds.GREEN)
            Leds.set_color(Leds.RIGHT, Leds.GREEN)

            self.cradle.stop_action = 'hold'
            self.grabber.stop_action = 'hold'
            self.cs_arm.stop_action = 'hold'

            self.cradle.position = 0
            self.grabber.position = 0
            self.cs_arm.position = 0

        Sound.beep()

    def check_peripherals(self):
        """
        Checks all peripherals (sensors & motors) are connected properly
        :return: boolean connection flag (if False then exit())
        """
        all_connected = True
        for p in self.peripherals:
            if not p.connected:
                print('%s not connected properly' % p)
                all_connected = False

        if not all_connected:
            print('Exiting...')
            exit()

    def exit(self, stall_flag=False):
        """
        Custom exit method to reposition motors back to starting position and ensure safe shutdown
        :param stall_flag: boolean if exiting due to motor stall
        :return:
        """
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        Leds.set_color(Leds.RIGHT, Leds.GREEN)

        if not stall_flag:
            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(0)
            # self.cradle.run_to_abs_pos(position_sp=0, speed_sp=self.cradle_speed)
            # self.cradle.wait_for_position(0)
            self.grabber.run_to_abs_pos(position_sp=0, speed_sp=self.grabber_speed, ramp_down_sp=50)
            self.grabber.wait_for_position(0)

        sleep(1)

        self.cradle.stop_action = 'coast'
        self.cradle.run_timed(time_sp=1, speed_sp=1)
        self.grabber.stop_action = 'coast'
        self.grabber.run_timed(time_sp=1, speed_sp=1)
        self.cs_arm.stop_action = 'coast'
        self.cs_arm.run_timed(time_sp=1, speed_sp=1)
        print()
        print()
        Sound.tone([(800, 100, 0), (600, 150, 0), (400, 100, 0)]).wait()
        exit()

    def rotate_cradle(self, angle=90):
        """
        Rotates the cradle by the provided angle
        :param angle: rotation angle in degrees
        :return: None
        """
        # 400 is 1/4 turn - 13.333:1 gear ratio
        mod_angle = angle * (40 / 9)
        pos = self.cradle.position + mod_angle
        self.cradle.run_to_abs_pos(position_sp=pos, speed_sp=self.cradle_speed, ramp_down_sp=100)
        self.cradle.wait_for_position(pos)

    def grab_cube(self):
        """
        Rotates the cube in the x direction
        :return: None
        """
        self.grabber.run_to_abs_pos(position_sp=self.gbr_grab_pos, speed_sp=self.grabber_speed * 1.5)
        self.grabber.wait_for_position(self.gbr_grab_pos)

        self.grabber.run_to_abs_pos(position_sp=-10, speed_sp=self.grabber_speed * 1.5)
        self.grabber.wait_for_position(-10)

        self.grabber.run_to_abs_pos(position_sp=self.gbr_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_guard_pos)

        sleep(0.05)

    def increment_progressbar(self):
        """
        Increments the progressbar when scanning the cube to display progress to the user
        :return: None
        """
        # Progressbar will change width depending on console size
        dims = get_terminal_size()

        if dims[0] > 64:
            progressbar_width = 54
        else:
            progressbar_width = dims[0] - 10

        # Increment number of scanned cubies, and scale it for sizing
        self._scanned_cubies += 1
        progress = int(self._scanned_cubies / (54 / progressbar_width))

        stdout.write('\r|')
        stdout.write('#' * progress)
        stdout.write('-' * (progressbar_width - progress))
        stdout.write('| %.2f%%' % ((self._scanned_cubies / 54) * 100))
        stdout.flush()

    def scan_up_face(self):
        """
        Scans the top face of the cube
        :return: None
        """
        middle = []
        corner = []

        # Moves the grabber out of the way
        self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_no_guard_pos)

        for i in range(4):
            # Middle
            self.cs_arm.run_to_abs_pos(position_sp=self.cs_mid_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_mid_pos)
            middle.append(self.color_scan_dict[self.color_sensor.value()])

            self.increment_progressbar()

            # Corner
            self.rotate_cradle(45)

            self.cs_arm.run_to_abs_pos(position_sp=self.cs_cor_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_cor_pos)

            # Checks that the color sensor is not reading no color or too dark a value
            if self.color_sensor.value() != (0 or 1):
                corner.append(self.color_scan_dict[self.color_sensor.value()])
            else:
                # Currently just exits the program if an extreme value is read
                print('Extreme Color value: %s' % str(Color(self.color_sensor.value())))
                exit()
            self.increment_progressbar()

            # Prep for next middle
            self.rotate_cradle(45)

        # Read centre cubie
        self.cs_arm.run_to_abs_pos(position_sp=self.cs_cen_pos, speed_sp=self.cs_speed)
        self.cs_arm.wait_for_position(self.cs_cen_pos)
        centre = self.color_scan_dict[self.color_sensor.value()]

        self.increment_progressbar()

        '''
        The face is scanned in this order:
            1 1 0
            2 C 0
            2 3 3
        '''

        return corner[1], middle[1], corner[0], middle[2], centre, middle[0], corner[2], middle[3], corner[3]

    def scan_cube(self):
        """
        Scans all 6 faces and returns the cube's position

        - X X X Y X X X
        U F D B - R - L    <---- Initial State
        L B R F - D - U   <---- Final State!!

        :param:
        :return: cube position as string
        """

        print("Scanning Rubik's Cube...")

        sides = [[], [], [], [], [], []]

        # The scanning process can be simulated for testing purposes
        if not self.simulated:

            # Move grabber out of the way
            self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed / 2)
            self.grabber.wait_for_position(self.gbr_no_guard_pos)

            for i in range(len(sides)):
                sides[i] = self.scan_up_face()

                self.cs_arm.run_to_abs_pos(position_sp=-300, speed_sp=self.cs_speed)
                self.cs_arm.wait_for_position(-300)

                if i == 3:
                    self.rotate_cradle()

                if i < 5:
                    self.grab_cube()

                if i == 4:
                    self.grab_cube()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
        else:
            for i in range(54):
                sleep(0.005)
                self.increment_progressbar()

            sides = SOLVED_SIDES

        color_validation_dict = {}
        for s in sides:
            for c in s:
                try:
                    color_validation_dict[c] += 1
                except KeyError:
                    color_validation_dict[c] = 1

        for key, value in color_validation_dict.items():
            if value != 9:
                print('\nInvalid number of %s facelets scanned (%i)' % (key.name, value))
                for k, v in color_validation_dict.items():
                    print('%s: %i' % (k.name, v))
                self.exit()
                exit()

    # These transformations align the cubes faces correctly, as they are inherently rotated when scanning the cube
        sides[0] = sides[0][6:7] + sides[0][3:4] + sides[0][0:1] + sides[0][7:8] + sides[0][4:5] + sides[0][1:2] + \
            sides[0][8:9] + sides[0][5:6] + sides[0][2:3]

        sides[1] = sides[1][6:7] + sides[1][3:4] + sides[1][0:1] + sides[1][7:8] + sides[1][4:5] + sides[1][1:2] + \
            sides[1][8:9] + sides[1][5:6] + sides[1][2:3]

        sides[2] = sides[2][6:7] + sides[2][3:4] + sides[2][0:1] + sides[2][7:8] + sides[2][4:5] + sides[2][1:2] + \
            sides[2][8:9] + sides[2][5:6] + sides[2][2:3]

        sides[3] = sides[3][6:7] + sides[3][3:4] + sides[3][0:1] + sides[3][7:8] + sides[3][4:5] + sides[3][1:2] + \
            sides[3][8:9] + sides[3][5:6] + sides[3][2:3]

        # Makes sure all the lists of colors are split down to form one list (Cube._pos)
        cube_pos = []
        for side in sides:
            for i in side:
                cube_pos.append(Color(i).value)

        # Re-orders the cube sides to match the ordering of the cube position variable
        corrected_cube_pos = cube_pos[45:] + cube_pos[0:3] + cube_pos[27:30] + cube_pos[18:21] + \
            cube_pos[9:12] + cube_pos[3:6] + cube_pos[30:33] + cube_pos[21:24] + \
            cube_pos[12:15] + cube_pos[6:9] + cube_pos[33:36] + cube_pos[24:27] + \
            cube_pos[15:18] + cube_pos[36:45]

        print('\n')
        return corrected_cube_pos

    # Robot moves
    def r_move_d(self):
        # Set guards to block position
        self.grabber.run_to_abs_pos(position_sp=self.gbr_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_guard_pos)

        # Rotate Cradle -90
        self.rotate_cradle(-100)
        self.rotate_cradle(15)
        self.rotate_cradle(-5)

    def r_move_not_d(self):
        # Set guards to block position
        self.grabber.run_to_abs_pos(position_sp=self.gbr_guard_pos, speed_sp=self.grabber_speed)
        self.grabber.wait_for_position(self.gbr_guard_pos)

        # Rotate Cradle 90
        self.rotate_cradle(100)
        self.rotate_cradle(-15)
        self.rotate_cradle(5)

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
        self.rotate_cradle()

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
        # Rotate Cradle 180
        self.rotate_cradle(180)

    # Allows any valid move to be actuated by passing a string in
    def run_move_method(self, move):
        try:
            method = getattr(Robot, 'r_move_' + move)
            method(self)
        except AttributeError as e:
            print('r_move failed: \'' + move + '\' | ' + str(e))
            exit()

    # Allows valid lists of moves to be passed in and actuated
    def run_move_sequence(self, move_chain):
        for move in move_chain:
            self.run_move_method(move)
            print(move, end=', ')

    def test(self):
        for j in range(2):
            self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed / 2)
            self.grabber.wait_for_position(self.gbr_no_guard_pos)

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(0)

            self.grab_cube()
            self.grab_cube()

            self.grabber.run_to_abs_pos(position_sp=self.gbr_no_guard_pos, speed_sp=self.grabber_speed / 2)
            self.grabber.wait_for_position(self.gbr_no_guard_pos)

            self.cs_arm.run_to_abs_pos(position_sp=-350, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(-350)

            self.grab_cube()
            self.grab_cube()
