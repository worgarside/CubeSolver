import socket

from robot.robot_class import Robot

IP_DICT = {
    'WILLS-SURFACE @ ONEPLUS 3': '192.168.43.188',
    'WILLS-DESKTOP @ HOME': '192.168.0.21',
}


def create_socket():
    conn = socket.socket()

    print('Connecting to %s:%s' % (IP_DICT['WILLS-DESKTOP @ HOME'], 3000))
    conn.connect((IP_DICT['WILLS-DESKTOP @ HOME'], 3000))
    print('Connected!')
    return conn


def create_robot():
    simulation = False
    robot = Robot(simulation)
    robot.init_motors()
    return robot


def main():
    conn = create_socket()
    robot = create_robot()

    pos_str = ''.join(robot.scan_cube())
    conn.send(pos_str.encode())

    robot.exit()


if __name__ == '__main__':
    main()
