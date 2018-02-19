from cube.cube_class import Cube
import colorama
from robot.robot_class import Robot


def main():
    simulation = False
    robot = Robot()
    robot.init_motors(simulation)
    pos = robot.scan_cube(simulation)
    cube = Cube(pos)
    colorama.init()
    print(cube)
    robot.exit()


if __name__ == '__main__':
    main()
