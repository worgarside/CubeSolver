#!/usr/bin/env python3

import data
from cube.cube_class import Cube

try:
    from robot.robot_class import Robot
    from ev3dev.helper import MotorStall
    robot_env = True
except FileNotFoundError as e:
    robot_env = False
    print(e)
from ev3dev.ev3 import Sound
import random


def solve_cube(rubiks_cube):
    # print(str(rubiks_cube) + '\n')
    rubiks_cube.generate_solve_sequences()
    # print(rubiks_cube.robot_solve_sequence)
    # print()


def randomize():
    moves = []
    for i in range(15):
        moves.append(random.choice(data.MOVES1))
    print(moves)


def main():
    if robot_env:
        simulate_init = True
        simulate_scan = True
        Sound.beep()
        rubiks_bot = Robot()
        try:
            rubiks_bot.init_motors(simulate_init)
            if simulate_scan:
                rubiks_cube = Cube(data.SOLVED_POS)
            else:
                rubiks_cube = Cube(rubiks_bot.scan_cube(simulate_scan))
            solve_cube(rubiks_cube)
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
        solve_cube(rubiks_cube)


if __name__ == '__main__':
    main()
