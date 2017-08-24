#!/usr/bin/env python3

from time import sleep
from cube_class import Color, Cube
# import ev3dev.ev3 as ev3
# from ev3dev.ev3 import Sound
# from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
# from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor


class Robot:
    # def __init__(self):
    #     self.cradle = LargeMotor(OUTPUT_A)
    #     self.swing_arm = LargeMotor(OUTPUT_B)
    #     self.cs_arm = MediumMotor(OUTPUT_C)
    #
    #     self.ts = ev3.TouchSensor()
    #     self.cs = ColorSensor()
    #     self.cs.mode = self.cs.MODE_COL_COLOR
    #
    #     self.cs_mid_pos = -1700
    #     self.cs_cor_pos = -1390
    #     self.cs_cen_pos = -2500
    #     self.cube_rot_speed = 30
    #     self.cs_speed = 500

    # def hold(self, message):
    #     print("\nHolding: '" + message + "'\n")
    #     Sound.tone([(800, 150, 0), (400, 150, 0), (800, 150, 0), (400, 150, 0)]).wait()
    #     while self.ts.value() != 1:
    #         pass

    # def init_motors(self):
    #     self.cradle.stop_action = "coast"
    #     self.cradle.run_timed(time_sp=1, speed_sp=1)
    #     self.swing_arm.stop_action = "coast"
    #     self.swing_arm.run_timed(time_sp=1, speed_sp=1)
    #     self.cs_arm.stop_action = "coast"
    #     self.cs_arm.run_timed(time_sp=1, speed_sp=1)
    #
    #     while self.ts.value() != 1:
    #         ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
    #         ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)
    #
    #     ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    #     ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    #
    #     self.cradle.stop_action = "hold"
    #     self.swing_arm.stop_action = "hold"
    #     self.cs_arm.stop_action = "hold"
    #
    #     self.cradle.position = 0
    #     self.swing_arm.position = 0
    #     self.cs_arm.position = 0
    #
    #     Sound.beep()

    def scan_up_face(self):
        middle = []
        corner = []

        for i in range(4):
            # Middle
            self.cs_arm.run_to_abs_pos(position_sp=self.cs_mid_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_mid_pos)
            middle.append(Color(self.cs.value()))

            # Corner
            new_pos = self.cradle.position - 45
            self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed)
            self.cradle.wait_for_position(new_pos)

            self.cs_arm.run_to_abs_pos(position_sp=self.cs_cor_pos, speed_sp=self.cs_speed)
            self.cs_arm.wait_for_position(self.cs_cor_pos)
            corner.append(Color(self.cs.value()))

            # Prep for next middle
            new_pos = self.cradle.position - 45
            self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=self.cube_rot_speed)
            self.cradle.wait_for_position(new_pos)

        # Read centre cubie
        self.cs_arm.run_to_abs_pos(position_sp=self.cs_cen_pos, speed_sp=self.cs_speed)
        self.cs_arm.wait_for_position(self.cs_cen_pos)
        centre = Color(self.cs.value())

        # 1 1 0
        # 2 C 0
        # 2 3 3

        return corner[1], middle[1], corner[0], middle[2], centre, middle[0], corner[2], middle[3], corner[3]

    def scan_cube(self, scan=True):
        # Z Z Z Z Y Z Z Z
        # U L D R - F - B
        sides = [[], [], [], [], [], []]

        if scan:
            # Move swing arm out of the way
            self.swing_arm.run_to_abs_pos(position_sp=60, speed_sp=100)
            self.swing_arm.wait_for_stop()

            # Side 0 - UP
            sides[0] = self.scan_up_face()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed * 2)
            self.cs_arm.wait_for_position(0)

            new_pos = self.swing_arm.position - 360
            self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.swing_arm.wait_for_position(new_pos)

            # Side 1 - LEFT
            sides[1] = self.scan_up_face()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed * 2)
            self.cs_arm.wait_for_position(0)

            new_pos = self.swing_arm.position - 360
            self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.swing_arm.wait_for_position(new_pos)

            # Side 2 - DOWN
            sides[2] = self.scan_up_face()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed * 2)
            self.cs_arm.wait_for_position(0)

            new_pos = self.swing_arm.position - 360
            self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.swing_arm.wait_for_position(new_pos)

            # Side 3 - RIGHT
            sides[3] = self.scan_up_face()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed * 2)
            self.cs_arm.wait_for_position(0)

            new_pos = self.cradle.position - 90
            self.cradle.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.cradle.wait_for_position(new_pos)

            new_pos = self.swing_arm.position - 360
            self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.swing_arm.wait_for_position(new_pos)

            # Side 4 - FRONT
            sides[4] = self.scan_up_face()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed * 2)
            self.cs_arm.wait_for_position(0)

            new_pos = self.swing_arm.position - 720
            self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.swing_arm.wait_for_position(new_pos)

            # Side 5 - BACK
            sides[5] = self.scan_up_face()

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=self.cs_speed * 2)
            self.cs_arm.wait_for_position(0)
        else:
            sides = [(Color.YELLOW, Color.BLUE, Color.WHITE, Color.RED, Color.GREEN, Color.ORANGE, Color.RED, Color.GREEN, Color.GREEN), (Color.RED, Color.GREEN, Color.ORANGE, Color.YELLOW, Color.ORANGE, Color.WHITE, Color.RED, Color.GREEN, Color.YELLOW), (Color.YELLOW, Color.GREEN, Color.WHITE, Color.ORANGE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.BLUE, Color.WHITE), (Color.ORANGE, Color.BLUE, Color.BLUE, Color.YELLOW, Color.RED, Color.WHITE, Color.RED, Color.RED, Color.WHITE), (Color.BLUE, Color.YELLOW, Color.YELLOW, Color.ORANGE, Color.YELLOW, Color.YELLOW, Color.GREEN, Color.RED, Color.BLUE), (Color.GREEN, Color.WHITE, Color.GREEN, Color.ORANGE, Color.WHITE, Color.RED, Color.ORANGE, Color.WHITE, Color.BLUE)]

        # # rotate left cw
        # s = sides[1]
        # sides[1] = (s[6], s[3], s[0], s[7], s[4], s[1], s[8], s[5], s[2])
        #
        # # rotate right cw
        # s = sides[3]
        # sides[3] = (s[6], s[3], s[0], s[7], s[4], s[1], s[8], s[5], s[2])

        cube_pos = []
        for side in sides:
            for i in side:
                cube_pos.append(i)

        return cube_pos

    def exit(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=1000)
        self.cs_arm.wait_for_position(0)
        self.cradle.run_to_abs_pos(position_sp=0, speed_sp=500)
        self.cradle.wait_for_position(0)
        self.swing_arm.run_to_abs_pos(position_sp=0, speed_sp=100)
        self.swing_arm.wait_for_position(0)

        sleep(2)

        self.cradle.stop_action = "coast"
        self.cradle.run_timed(time_sp=1, speed_sp=1)
        self.swing_arm.stop_action = "coast"
        self.swing_arm.run_timed(time_sp=1, speed_sp=1)
        self.cs_arm.stop_action = "coast"
        self.cs_arm.run_timed(time_sp=1, speed_sp=1)
        Sound.tone([(800, 100, 0), (600, 150, 0), (400, 100, 0)]).wait()

def main():
    # Sound.beep()
    rubiks_bot = Robot()
    try:
        cube_scan = rubiks_bot.scan_cube(False)
        print(cube_scan)
        rubiks_cube = Cube(cube_scan)
        print(rubiks_cube)
    except KeyboardInterrupt:
        pass  # Stops immediate sys.exit to run custom exit function
    # rubiks_bot.exit()

if __name__ == "__main__":
    main()
