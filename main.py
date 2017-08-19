#!/usr/bin/env python3

from enum import Enum
import ev3dev.ev3 as ev3
from ev3dev.ev3 import Sound
from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.helper import LargeMotor, MediumMotor, ColorSensor


class Rot(Enum):
    CLOCKWISE = "normal"
    COUNTER_CLOCKWISE = "inversed"


class Robot:
    def __init__(self):
        self.y_mtr = LargeMotor(OUTPUT_A)
        self.swing_arm = LargeMotor(OUTPUT_B)
        self.cs_mtr = MediumMotor(OUTPUT_C)

        self.ts = ev3.TouchSensor()
        self.cs = ev3.ColorSensor()

        # Needs a harsh stop to ensure alignment is correct
        self.y_mtr.stop_action = "brake"
        self.swing_arm.stop_action = "brake"

    def init_motors(self):
        # print("y_mtr: " + str(self.y_mtr.position))
        # print("swing_arm: " + str(self.swing_arm.position))

        Sound.beep()
        
        self.y_mtr.stop_action = "coast"
        self.swing_arm.stop_action = "coast"
        self.y_mtr.run_timed(time_sp=1, speed_sp=1)
        self.swing_arm.run_timed(time_sp=1, speed_sp=1)

        while self.ts.value() != 1:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)

        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        self.y_mtr.stop_action = "brake"
        self.swing_arm.stop_action = "brake"

        self.y_mtr.position = 0
        self.swing_arm.position = 0

        # print("\ny_mtr: " + str(self.y_mtr.position))
        # print("swing_arm: " + str(self.swing_arm.position))

        self.cs_mtr.run_timed(time_sp=2500, speed_sp=1000)
        self.cs_mtr.wait_for_stop()
        self.cs_mtr.run_to_rel_pos(position_sp=-75, speed_sp=100)

        Sound.beep()

    def scan_cube(self):
        self.cs_mtr.run_to_rel_pos(position_sp=-1500, speed_sp=1000)
        print(self.cs.color())


def main():
    rubiks_bot = Robot()
    rubiks_bot.init_motors()
    rubiks_bot.scan_cube()


if __name__ == "__main__":
    main()
