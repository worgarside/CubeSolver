from cube.cube_class import Cube
import colorama
from robot.robot_class import Robot


def main():
    robot = Robot()
    robot.init_motors(False)
    # robot.rotate_cradle(180)
    # time.sleep(5)
    # robot.grab_cube()
    pos = robot.scan_cube()
    cube = Cube(pos)
    print(pos)
    colorama.init()
    print(cube)
    robot.exit()


if __name__ == '__main__':
    main()
