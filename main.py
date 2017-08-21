#!/usr/bin/env python3

from enum import Enum
import ev3dev.ev3 as ev3
import time
from cube_class import Cube
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
        self.cs = ColorSensor()
        self.cs.mode = self.cs.MODE_RGB_RAW
        # self.cs.mode = self.cs.MODE_COL_COLOR

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

        self.cs_mtr.run_timed(time_sp=3000, speed_sp=1000)
        self.cs_mtr.wait_for_stop()
        self.cs_mtr.run_to_rel_pos(position_sp=-75, speed_sp=100)
        self.cs_mtr.position = 0

        Sound.beep()

    def scan_cube(self):
        cs_mid_pos = -1700
        cs_cor_pos = -1380
        cs_cen_pos = -2500
        cube_rot_speed = 30
        cs_speed = 500
        # ??: centre

        # Move swing arm out of the way
        self.swing_arm.run_to_abs_pos(position_sp=60, speed_sp=100)
        self.swing_arm.wait_for_stop()

        # Line up and read middle #1
        self.cs_mtr.run_to_abs_pos(position_sp=cs_mid_pos, speed_sp=cs_speed*2)
        self.cs_mtr.wait_for_stop()
        top_mid1 = self.cs.value()
        print("top_mid1:" + str(top_mid1))
        Sound.beep()

        # Line up with/rotate to corner #1
        self.cs_mtr.run_to_abs_pos(position_sp=cs_cor_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Read corner #1
        top_cor1 = self.cs.value()
        print("top_cor1:" + str(top_cor1))
        Sound.beep()

        # Rotate to middle
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Line up with and read middle #2
        self.cs_mtr.run_to_abs_pos(position_sp=cs_mid_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        top_mid2 = self.cs.value()
        print("top_mid2:" + str(top_mid2))
        Sound.beep()

        # Line up with/rotate to corner #2
        self.cs_mtr.run_to_abs_pos(position_sp=cs_cor_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Read corner #2
        top_cor2 = self.cs.value()
        print("top_cor2:" + str(top_cor2))
        Sound.beep()

        # Rotate to middle
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Line up with and read middle #3
        self.cs_mtr.run_to_abs_pos(position_sp=cs_mid_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        top_mid3 = self.cs.value()
        print("top_mid3:" + str(top_mid3))
        Sound.beep()

        # Line up with/rotate to corner #3
        self.cs_mtr.run_to_abs_pos(position_sp=cs_cor_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Read corner #3
        top_cor3 = self.cs.value()
        print("top_cor3:" + str(top_cor3))
        Sound.beep()

        # Rotate to middle #4
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Line up with and read middle #2
        self.cs_mtr.run_to_abs_pos(position_sp=cs_mid_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        top_mid4 = self.cs.value()
        print("top_mid4:" + str(top_mid4))
        Sound.beep()


        # Line up with/rotate to corner #4
        self.cs_mtr.run_to_abs_pos(position_sp=cs_cor_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)

        # Read corner #4
        top_cor4 = self.cs.value()
        print("top_cor4:" + str(top_cor4))
        Sound.beep()

        # Rotate back to 0
        new_pos = self.y_mtr.position + 45
        self.y_mtr.run_to_abs_pos(position_sp=new_pos, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(new_pos)
        self.y_mtr.position = 0

        # Read centre cubie
        self.cs_mtr.run_to_abs_pos(position_sp=cs_cen_pos, speed_sp=cs_speed)
        self.cs_mtr.wait_for_stop()
        top_cen = self.cs.value()
        print("top_cen:" + str(top_cen))
        Sound.beep()


        time.sleep(2)

        self.cs_mtr.run_to_abs_pos(position_sp=0, speed_sp=cs_speed*2)

        self.y_mtr.run_to_abs_pos(position_sp=0, speed_sp=cube_rot_speed)
        self.y_mtr.wait_for_stop()
        self.y_mtr.wait_for_position(0)

        self.swing_arm.run_to_abs_pos(position_sp=0, speed_sp=20)






def main():
    rubiks_bot = Robot()
    # rubiks_bot.swing_arm.run_timed(time_sp=5000, speed_sp=100)
    # rubiks_bot.swing_arm.wait_for_stop()
    # rubiks_bot.swing_arm.run_timed(time_sp=5000, speed_sp=100)
    # rubiks_bot.swing_arm.wait_for_stop()
    rubiks_bot.init_motors()
    rubiks_bot.scan_cube()
    # cube = Cube()


if __name__ == "__main__":
    main()
