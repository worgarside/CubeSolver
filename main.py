#!/usr/bin/env python3

from cube_class import Cube
import data
try:
    from robot_class import Robot
    from ev3dev.helper import MotorStall
    robot_env = True
except FileNotFoundError as e:
    robot_env = False
    print(e)
from ev3dev.ev3 import Sound


def main():
    if robot_env:
        simulate_init = False
        simulate_scan = True
        Sound.beep()
        rubiks_bot = Robot()
        try:
            rubiks_bot.init_motors(simulate_init)
            rubiks_cube = Cube(rubiks_bot.scan_cube(simulate_scan))

            print(rubiks_cube)
            rubiks_cube.generate_solve_sequences()
            print(rubiks_cube.robot_solve_sequence)
            rubiks_bot.run_move_sequence(rubiks_cube.robot_solve_sequence)

        except KeyboardInterrupt:
            pass  # Stops immediate sys.exit to run custom exit function
        except TypeError as e2:
            print('TypeError: ' + str(e2))
        except MotorStall as e3:
            print('MotorStall: ' + str(e3))
            rubiks_bot.exit(True)
        rubiks_bot.exit()
    else:
        rubiks_cube = Cube(data.SOLVED_POS)
        print(rubiks_cube)
        rubiks_cube.generate_solve_sequences()
        # print(rubiks_cube.robot_solve_sequence)


if __name__ == '__main__':
    main()
    # import random
    # print('[', end='')
    # for i in range(30):
    #     print('\'' + str(random.choice(data.MOVES1)) + '\', ', end='')
    # print(']')
