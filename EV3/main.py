import pickle
import socket
from time import sleep

from ev3dev.ev3 import Sound

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
    Sound.speak('connected to server')
    sleep(1.5)
    return conn


def create_robot():
    simulation = True
    robot = Robot(simulation)
    robot.init_motors(True)
    return robot


def main():
    conn = create_socket()
    robot = create_robot()
    #
    pos_str = ''.join(robot.scan_cube())
    conn.send(pos_str.encode())

    sequence = ''
    sequence_received = False
    while not sequence_received:
        data = conn.recv(1024)
        sequence = pickle.loads(data)
        if sequence != '':
            sequence_received = True

    print(sequence)

    robot.run_move_sequence(sequence)
    robot.exit()


if __name__ == '__main__':
    main()
