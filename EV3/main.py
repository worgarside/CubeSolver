from robot.robot_class import Robot


def main():
    simulation = False
    robot = Robot()
    robot.init_motors(simulation)
    pos = robot.scan_cube(simulation)
    # send pos to PC
    print(pos)
    robot.exit()


if __name__ == '__main__':
    main()
