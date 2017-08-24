#!/usr/bin/env python3

from cube_class import Side, Color
import ev3dev.ev3 as ev3
from ev3dev.ev3 import Sound
from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor


class Robot:
    def __init__(self):
        self.cradle = LargeMotor(OUTPUT_A)
        self.swing_arm = LargeMotor(OUTPUT_B)
        self.cs_arm = MediumMotor(OUTPUT_C)

        self.ts = ev3.TouchSensor()
        self.cs = ColorSensor()
        self.cs.mode = self.cs.MODE_COL_COLOR

    def hold(self, message):
        print("\nHolding: '" + message + "'\n")
        Sound.tone([(800, 150, 0), (400, 150, 0), (800, 150, 0), (400, 150, 0)]).wait()
        while self.ts.value() != 1:
            pass

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

    def scan_up_face(self):
        cs_mid_pos = -1700
        cs_cor_pos = -1390
        cs_cen_pos = -2500
        cube_rot_speed = 30
        cs_speed = 500

        middle = []
        corner = []

        for i in range(4):
            # Middle
            self.cs_arm.run_to_abs_pos(position_sp=cs_mid_pos, speed_sp=cs_speed)
            self.cs_arm.wait_for_position(cs_mid_pos)
            Sound.beep()
            middle.append(Color(self.cs.value()))

            # Corner
            next_pos = self.cradle.position - 45
            self.cradle.run_to_abs_pos(position_sp=next_pos, speed_sp=cube_rot_speed)
            self.cradle.wait_for_position(next_pos)

            self.cs_arm.run_to_abs_pos(position_sp=cs_cor_pos, speed_sp=cs_speed)
            self.cs_arm.wait_for_position(cs_cor_pos)
            Sound.beep()
            corner.append(Color(self.cs.value()))

            # Prep for next middle
            next_pos = self.cradle.position - 45
            self.cradle.run_to_abs_pos(position_sp=next_pos, speed_sp=cube_rot_speed)
            self.cradle.wait_for_position(next_pos)

        # Read centre cubie
        self.cs_arm.run_to_abs_pos(position_sp=cs_cen_pos, speed_sp=cs_speed)
        self.cs_arm.wait_for_position(cs_cen_pos)
        Sound.beep()
        centre = Color(self.cs.value())

        # 1 1 0
        # 2 C 0
        # 2 3 3

        return corner[1], middle[1], corner[0], middle[2], middle[2], centre, middle[0], corner[2], middle[3], corner[3]

    def scan_cube(self):

        # Z Z Z Z Y Z Z Z
        # U L D R - F - B

        cube_rot_speed = 30
        cs_speed = 500

        # Move swing arm out of the way
        self.swing_arm.run_to_abs_pos(position_sp=60, speed_sp=100)
        self.swing_arm.wait_for_stop()

        sides = [[], [], [], [], [], []]

        for side in Side:
            sides[side.value] = self.scan_up_face()

            print(sides[side.value][:3])
            print(sides[side.value][4:7])
            print(sides[side.value][7:])

            # self.hold("CS to 0")

            self.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=cs_speed * 2)
            self.cs_arm.wait_for_stop()
            self.cs_arm.wait_for_position(0)

            # self.hold("Swing Arm -360deg")

            new_pos = self.swing_arm.position - 360
            self.swing_arm.run_to_abs_pos(position_sp=new_pos, speed_sp=200)
            self.swing_arm.wait_for_position(new_pos)
            self.swing_arm.position = 60

            # self.hold("Start next face")

        self.cradle.run_to_abs_pos(position_sp=0, speed_sp=cube_rot_speed)
        self.cradle.wait_for_position(0)


def main():
    Sound.beep()
    rubiks_bot = Robot()
    try:
        rubiks_bot.init_motors()
        rubiks_bot.scan_cube()
    except KeyboardInterrupt:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        rubiks_bot.cs_arm.run_to_abs_pos(position_sp=0, speed_sp=1000)
        rubiks_bot.cs_arm.wait_for_position(0)
        rubiks_bot.cradle.run_to_abs_pos(position_sp=0, speed_sp=500)
        rubiks_bot.cradle.wait_for_position(0)
        rubiks_bot.swing_arm.run_to_abs_pos(position_sp=0, speed_sp=100)
        rubiks_bot.swing_arm.wait_for_position(0)

        rubiks_bot.cradle.stop_action = "coast"
        rubiks_bot.cradle.run_timed(time_sp=1, speed_sp=1)
        rubiks_bot.swing_arm.stop_action = "coast"
        rubiks_bot.swing_arm.run_timed(time_sp=1, speed_sp=1)
        rubiks_bot.cs_arm.stop_action = "coast"
        rubiks_bot.cs_arm.run_timed(time_sp=1, speed_sp=1)
        Sound.tone([(800, 175, 0), (600, 200, 0), (400, 175, 0)]).wait()


if __name__ == "__main__":
    main()
