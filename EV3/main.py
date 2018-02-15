from robot.robot_class import Robot


def main():
    robot = Robot()
    robot.init_motors(False)
    robot.rotate_cradle(180)
    robot.grab_cube()


if __name__ == '__main__':
    main()
