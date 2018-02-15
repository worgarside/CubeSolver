import time

from robot.robot_class import Robot


def main():
    robot = Robot()
    robot.init_motors(False)
    # robot.rotate_cradle(180)
    # time.sleep(5)
    # robot.grab_cube()
    robot.scan_cube()
    robot.exit()


if __name__ == '__main__':
    main()
