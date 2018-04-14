from os import get_terminal_size
from os.path import dirname
from sys import stdout, path
from time import sleep

from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.ev3 import Sound, Leds, TouchSensor, ColorSensor
from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor

path.append(dirname(path[0]))
__package__ = "robot"

from cube.cube_class import Color

SOLVED_FACES = [(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE,
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

# All the values used for setting the motor's 'keyframe' positions
# CS = Color Sensor; Grabber/GBR = the X-Move Arm; Cradle = Cradle
CS_MID_POS = -1650
CS_COR_POS = -1350
CS_CEN_POS = -2300
CRADLE_SPEED = 1020
CS_SPEED = 1020
GRABBER_SPEED = 325
GBR_NO_GUARD_POS = 65
GBR_GUARD_POS = -35
GBR_GRAB_POS = -90

# Converts the Color Sensor values to type of Color object
COLOR_SCAN_DICT = {0: Color.NONE, 1: Color.DARK, 2: Color.BLUE, 3: Color.GREEN, 4: Color.YELLOW,
                   5: Color.RED, 6: Color.WHITE, 7: Color.ORANGE}


class Robot:
    """A LEGO EV3 Robot with 3 motors, a colour sensor, and a touch sensor.

    """

    def __init__(self, simulation=False):
        """
        Initialises the Robot by connecting to peripherals and initialising motors
        :param simulation: Some of the Robot's functions can be simulated for testing to save time
            (e.g. avoid re-scanning Cube every time)
        """

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
        self._scanned_cubies = 0

        if not self.simulated:
            self.check_peripherals()
            self.init_motors()

    def init_motors(self):
        """
        Allows user to manually position the motors at their starting position
        """

        # Removes all braking resistance by running in 'coast' mode for 1ms
        self.set_motor_brakes(self.cradle, 'coast')
        self.set_motor_brakes(self.grabber, 'coast')
        self.set_motor_brakes(self.cs_arm, 'coast')

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
        """
        all_connected = True
        for p in self.peripherals:
            if not p.connected:
                print('%s not connected properly' % p)
                # Doesn't exit immediately in case there is more than one problem
                all_connected = False

        exit() if not all_connected else None

    def shutdown(self, stall_flag=False, silent=False):
        """
        Custom exit method to reposition motors back to starting position and ensure safe shutdown
        :param silent: gives the option to disable the beeps and motor movements
        :param stall_flag: boolean if exiting due to motor stall, if they are stalled they shouldn't be repositioned
        """
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        Leds.set_color(Leds.RIGHT, Leds.GREEN)

        if not stall_flag and not silent:
            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=CS_SPEED)
            self.cs_arm.wait_for_position(0)
            self.grabber.run_to_abs_pos(position_sp=0, speed_sp=GRABBER_SPEED, ramp_down_sp=50)
            self.grabber.wait_for_position(0)

        sleep(1)

        self.set_motor_brakes(self.cradle, 'coast')
        self.set_motor_brakes(self.grabber, 'coast')
        self.set_motor_brakes(self.cs_arm, 'coast')

        if not silent:
            Sound.tone([(800, 100, 0), (600, 150, 0), (400, 100, 0)]).wait()
        exit()

    def rotate_cradle(self, angle=90):
        """
        Rotates the cradle by the provided angle
        :param angle: rotation angle in degrees
        """
        # 400 is 1/4 turn - 13.333:1 gear ratio
        mod_angle = angle * (40 / 9)
        self.cradle.reset()
        self.set_motor_brakes(self.cradle, 'hold')
        self.cradle.speed_sp = CRADLE_SPEED
        pos = self.cradle.position + mod_angle
        self.cradle.run_to_abs_pos(position_sp=pos)
        self.cradle.wait_until_not_moving()
        sleep(0.05)

    def grab_cube(self):
        """
        Rotates the cube in the x direction by moving the grabber to its 'keyframe' points
        """
        self.grabber.run_to_abs_pos(position_sp=GBR_GRAB_POS, speed_sp=GRABBER_SPEED * 1.5)
        self.grabber.wait_for_position(GBR_GRAB_POS)

        self.grabber.run_to_abs_pos(position_sp=20, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(0)

        self.grabber.run_to_abs_pos(position_sp=GBR_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_GUARD_POS)

        sleep(0.05)

    def increment_progressbar(self):
        """
        Increments the progressbar when scanning the cube to display progress to the user
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
        """

        middle = []
        corner = []

        # Moves the grabber out of the way
        self.grabber.run_to_abs_pos(position_sp=GBR_NO_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_NO_GUARD_POS)

        for i in range(4):
            # Middle
            self.cs_arm.run_to_abs_pos(position_sp=CS_MID_POS, speed_sp=CS_SPEED)
            self.cs_arm.wait_for_position(CS_MID_POS)
            middle.append(COLOR_SCAN_DICT[self.color_sensor.value()])

            self.increment_progressbar()

            # Corner
            self.rotate_cradle(45)

            self.cs_arm.run_to_abs_pos(position_sp=CS_COR_POS, speed_sp=CS_SPEED)
            self.cs_arm.wait_for_position(CS_COR_POS)

            # Checks that the color sensor is not reading no color or too dark a value
            if self.color_sensor.value() not in [0, 1]:
                corner.append(COLOR_SCAN_DICT[self.color_sensor.value()])
            else:
                print('Extreme Color value: %s' % str(Color(self.color_sensor.value())))
                self.shutdown()
            self.increment_progressbar()

            # Prep for next middle
            self.rotate_cradle(45)

        # Read centre cubie
        self.cs_arm.run_to_abs_pos(position_sp=CS_CEN_POS, speed_sp=CS_SPEED)
        self.cs_arm.wait_for_position(CS_CEN_POS)
        centre = COLOR_SCAN_DICT[self.color_sensor.value()]

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

        - X X X Y X X X     <---- The moves performed in process
        U F D B - R - L    <---- Face scan order
        L B R F - D - U   <---- The faces that are in the original faces' positions at the end

        :return: cube position as string
        """

        print("Scanning Rubik's Cube...")

        faces = [[], [], [], [], [], []]

        # The scanning process can be simulated for testing purposes
        if not self.simulated:

            # Move grabber out of the way
            self.grabber.run_to_abs_pos(position_sp=GBR_NO_GUARD_POS, speed_sp=GRABBER_SPEED / 2)
            self.grabber.wait_for_position(GBR_NO_GUARD_POS)

            for i in range(len(faces)):
                faces[i] = self.scan_up_face()

                self.set_motor_brakes(self.cradle, 'coast')

                self.cs_arm.run_to_abs_pos(position_sp=-300, speed_sp=CS_SPEED)
                self.cs_arm.wait_for_position(-300)

                # Rotate 90 after fourth face to get to L-face and R-face
                if i == 3:
                    self.rotate_cradle()

                # X-move on all faces apart from last one
                if i < 5:
                    self.grab_cube()

                # Extra X-move on fifth face to get from UP to DOWN
                if i == 4:
                    self.grab_cube()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=CS_SPEED)
        else:
            for i in range(54):
                sleep(0.005)
                self.increment_progressbar()

            faces = SOLVED_FACES

        # Validates scan by creating a dictionary of Colors and checking all quantities = 9
        color_validation_dict = {}
        for face in faces:
            for color in face:
                try:
                    color_validation_dict[color] += 1
                except KeyError:
                    color_validation_dict[color] = 1
        for key, value in color_validation_dict.items():
            if value != 9:
                print('\nInvalid number of %s facelets scanned (%i)' % (key.name, value))
                for k, v in color_validation_dict.items():
                    print('%s: %i' % (k.name, v))
                self.shutdown()

        # These transformations align the cubes faces correctly, as they are rotated when scanning the cube
        # (i.e. the Cube is transformed during the process, so must be transformed back)
        faces[0] = faces[0][6:7] + faces[0][3:4] + faces[0][0:1] + faces[0][7:8] + faces[0][4:5] + faces[0][1:2] + \
            faces[0][8:9] + faces[0][5:6] + faces[0][2:3]

        faces[1] = faces[1][6:7] + faces[1][3:4] + faces[1][0:1] + faces[1][7:8] + faces[1][4:5] + faces[1][1:2] + \
            faces[1][8:9] + faces[1][5:6] + faces[1][2:3]

        faces[2] = faces[2][6:7] + faces[2][3:4] + faces[2][0:1] + faces[2][7:8] + faces[2][4:5] + faces[2][1:2] + \
            faces[2][8:9] + faces[2][5:6] + faces[2][2:3]

        faces[3] = faces[3][6:7] + faces[3][3:4] + faces[3][0:1] + faces[3][7:8] + faces[3][4:5] + faces[3][1:2] + \
            faces[3][8:9] + faces[3][5:6] + faces[3][2:3]

        # Makes sure all the lists of colors are split down to form one list (Cube._pos)
        cube_pos = []
        for face in faces:
            for i in face:
                cube_pos.append(Color(i).value)

        # Re-orders the cube faces to match the ordering of the cube position variable
        corrected_cube_pos = cube_pos[45:] + cube_pos[0:3] + cube_pos[27:30] + cube_pos[18:21] + \
            cube_pos[9:12] + cube_pos[3:6] + cube_pos[30:33] + cube_pos[21:24] + \
            cube_pos[12:15] + cube_pos[6:9] + cube_pos[33:36] + cube_pos[24:27] + \
            cube_pos[15:18] + cube_pos[36:45]

        print('\n')
        return corrected_cube_pos

    # Robot moves
    def r_move_d(self):
        # Set guards to block position
        self.grabber.run_to_abs_pos(position_sp=GBR_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_GUARD_POS)

        # Rotate Cradle -90
        self.rotate_cradle(-90)

    def r_move_not_d(self):
        # Set guards to block position
        self.grabber.run_to_abs_pos(position_sp=GBR_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_GUARD_POS)

        # Rotate Cradle 90
        self.rotate_cradle()

    def r_move_d2(self):
        # Set guards to block position
        self.rotate_cradle(-180)

    def r_move_x(self):
        # Grab cube
        self.grab_cube()

    def r_move_x2(self):
        # Grab cube
        self.grab_cube()
        self.grab_cube()

    def r_move_y(self):
        # Remove guards
        self.grabber.run_to_abs_pos(position_sp=GBR_NO_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_NO_GUARD_POS)
        # Rotate Cradle 90
        self.rotate_cradle()

    def r_move_not_y(self):
        # Remove guards
        self.grabber.run_to_abs_pos(position_sp=GBR_NO_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_NO_GUARD_POS)
        # Rotate Cradle -90
        self.rotate_cradle(-90)

    def r_move_y2(self):
        # Remove guards
        self.grabber.run_to_abs_pos(position_sp=GBR_NO_GUARD_POS, speed_sp=GRABBER_SPEED)
        self.grabber.wait_for_position(GBR_NO_GUARD_POS)
        # Rotate Cradle 180
        self.rotate_cradle(180)

    def run_move_method(self, move):
        """
        Allows any valid move to be actuated by passing a string in
        :param move: The Move object to be performed on the Cube
        """
        try:
            method = getattr(Robot, 'r_move_' + move)
            method(self)
        except AttributeError as e:
            print('r_move failed: \'' + move + '\' | ' + str(e))
            exit()

    def run_move_sequence(self, move_sequence):
        """
        Allows valid lists of moves to be passed in and iterated through
        :param move_sequence: The sequence which is to be performed
        """
        for move in move_sequence:
            self.run_move_method(move)
            print(move, end=', ')

    @staticmethod
    def set_motor_brakes(motor, brake_method):
        """
        Set the stopping method of any motor
        :param motor: the motor to be updated
        :param brake_method: the method of choice to be set on the motor, passed in as a string
        """
        motor.stop_action = brake_method
        if brake_method == 'coast':
            motor.run_timed(time_sp=1, speed_sp=1)

    def show_off(self):
        """
        Play a tune and spin the Cube once it has been solved as a way to end the program
        """
        self.grabber.run_to_abs_pos(position_sp=GBR_NO_GUARD_POS, speed_sp=GRABBER_SPEED/4)
        self.grabber.wait_for_position(GBR_NO_GUARD_POS)
        self.cradle.run_to_rel_pos(position_sp=800, speed_sp=255)

        Sound.tone(
            [(987, 53, 53), (987, 53, 53), (987, 53, 53), (987, 428, 0), (784, 428, 0),
             (880, 428, 0), (987, 107, 214), (880, 107, 0), (987, 800, 0)]
        ).wait()

        self.cradle.wait_for_stop()
        self.set_motor_brakes(self.cradle, 'coast')
        self.set_motor_brakes(self.grabber, 'coast')
        self.set_motor_brakes(self.cs_arm, 'coast')
        self.shutdown(False, True)
