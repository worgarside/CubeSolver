from time import sleep
from ev3dev.ev3 import Sound, OUTPUT_A
from ev3dev.helper import LargeMotor

motor = LargeMotor(OUTPUT_A)
motor.stop_action = 'hold'

for i in range(16):
    motor.run_to_rel_pos(position_sp=200, speed_sp=510)
    motor.wait_until_not_moving()
    sleep(0.05)
    Sound.beep()

motor.stop_action = 'coast'
motor.run_timed(time_sp=1, speed_sp=1)
