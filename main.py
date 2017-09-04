#!/usr/bin/env python3

from cube_class import Cube
import data
try:
    from robot_class import Robot
    robot_env = True
except FileNotFoundError as e:
    robot_env = False
    print(e)
import primary_moves as pmove
from ev3dev.ev3 import Sound


def main():
    rubiks_cube = Cube(data.SOLVED_POS)
    # print(rubiks_cube)
    rubiks_cube.solve()
    print(rubiks_cube.robot_solve_sequence)

    for pm in rubiks_cube.color_solve_sequence:
        # rubiks_cube.robot_solve_sequence = []
        method = getattr(pmove, pm)
        method(rubiks_cube)
        print(pm)
        # print(rubiks_cube.robot_solve_sequence)

    print(rubiks_cube)
    print(rubiks_cube.robot_solve_sequence)


    if robot_env:
        simulate_bot = False
        Sound.beep()
        rubiks_bot = Robot()
        try:
            rubiks_bot.init_motors(simulate_bot)
            rubiks_bot.run_move_sequence(rubiks_cube.robot_solve_sequence)

        except KeyboardInterrupt:
            pass  # Stops immediate sys.exit to run custom exit function
        except TypeError as e2:
            print('TypeError: ' + str(e2))
        rubiks_bot.exit()


if __name__ == '__main__':
    main()
