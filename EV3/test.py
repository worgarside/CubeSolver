from time import sleep
from ev3dev.ev3 import Sound, OUTPUT_A
from ev3dev.helper import LargeMotor

motor = LargeMotor(OUTPUT_A)
motor.stop_action = 'hold'

motor.position = 0

for i in range(16):
    pos = motor.position
    new_pos = pos+200
    # motor.run_to_rel_pos(position_sp=200, speed_sp=510)
    motor.run_to_abs_pos(position_sp=new_pos, speed_sp=1020)
    motor.wait_until_not_moving()
    sleep(0.05)
    Sound.beep()
    print('%i: %i' % (i+1, motor.position))

motor.stop_action = 'coast'
motor.run_timed(time_sp=1, speed_sp=1)
