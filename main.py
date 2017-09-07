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
import random


def solve_cube(rubiks_cube):
    print(str(rubiks_cube) + '\n')
    # print('[', end='')
    # for p in rubiks_cube._pos:
    #     print(str(p) + ', ', end='')
    # print(']\n')

    rubiks_cube.generate_solve_sequences()
    print(rubiks_cube.robot_solve_sequence)
    print()


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
            # rubiks_cube = Cube(rubiks_bot.scan_cube(simulate_scan))
            rubiks_cube = Cube(data.MOVES10POS)
            print(rubiks_cube.digital_solve_sequence)
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
    # import random
    # print('[', end='')
    # for i in range(30):
    #     print('\'' + str(random.choice(data.MOVES1)) + '\', ', end='')
    # print(']')
