import datetime
import os
import pickle
import socket
from time import sleep, time

from ev3dev.ev3 import Sound
from ev3dev.helper import MotorStall

from robot_class import Robot

# Different IPs for different locations, saves having to re-enter them each time
IP_DICT = {
    'WILLS-SURFACE @ ONEPLUS 3': '192.168.43.188',
    'WILLS-DESKTOP @ HOME': '192.168.0.21',
    'WILLS-SURFACE @ EDGE LANE': '192.168.1.84',
    'WILLS-SURFACE @ LG V500': '192.168.56.1'
}

# the IP currently in use by the host computer
CURRENT_IP = IP_DICT['WILLS-SURFACE @ ONEPLUS 3']


def create_socket():
    """
    Creates a socket object, and waits for it to connect to the host computer
    :return: Socket connection object
    """
    print('Connecting to %s:%s..' % (CURRENT_IP, 3000), end='', flush=True)
    conn = socket.socket()
    try:
        conn.connect((CURRENT_IP, 3000))
    except TimeoutError:
        print('?')
        print('Connection timed out at ', end='')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        exit(1)

    print('!')
    Sound.speak('connected to server')
    sleep(1.5)
    return conn


def scan_cube(robot):
    """
    Call Robot's scan_cube method, and finds the average time of all successful scans for analysis
    :param robot: the Robot object which scans the Cube
    :return: Cube position string (54 chars, each one of the Color object names)
    """
    start_time = time()
    pos = robot.scan_cube()
    end_time = time()

    file_path = '%s/scan_times.csv' % os.path.abspath(os.path.dirname(__file__))
    with open(file_path) as csv_read:
        (avg_time_str, scan_count_str) = csv_read.readline().split(',')

    old_avg_time = float(avg_time_str)
    old_scan_count = int(scan_count_str)

    new_scan_time = end_time - start_time
    new_scan_count = old_scan_count + 1
    new_avg_time = ((old_avg_time * old_scan_count) + new_scan_time) / new_scan_count

    with open(file_path, 'wb') as csv_write:
        csv_write.write(bytes('%0.3f,%i' % (new_avg_time, new_scan_count), 'UTF-8'))

    if new_scan_time > new_avg_time:
        print('Scan time of %0.1fs was ~%0.1fs slower than average' % (new_scan_time, new_scan_time - new_avg_time))
    else:
        print('Scan time of %0.1fs was ~%0.1fs faster than average' % (new_scan_time, new_avg_time - new_scan_time))

    return pos


def main():
    conn = create_socket()
    robot = Robot()

    try:
        # Scan the Cube and transmits the position back to the host computer for processing
        pos = scan_cube(robot)
        pos_str = ''.join(pos)
        conn.send(pos_str.encode())

        sequence = ''
        sequence_received = False
        try:
            # Wait until data (presumably the solve sequence) is received
            while not sequence_received:
                data = conn.recv(1024)
                sequence = pickle.loads(data)
                if sequence != '':
                    sequence_received = True
        except EOFError:
            print('Host computer disconnected!')
            robot.shutdown()
        print(sequence)

        # Run the solve sequence then show off before shutting down
        robot.run_move_sequence(sequence)
        robot.show_off()
    except MotorStall as err:
        print('\n\n %s' % err)
        robot.shutdown()


if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    main()
