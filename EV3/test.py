from time import sleep

from ev3dev.ev3 import Sound
from ev3dev.helper import ColorSensor


color_sensor = ColorSensor()
color_scan_dict = {0: 'NONE', 1: 'DARK', 2: 'BLUE', 3: 'GREEN', 4: 'YELLOW',
                   5: 'RED', 6: 'WHITE', 7: 'ORANGE'}

while True:
    print('\n')
    Sound.beep()
    color_sensor.mode = color_sensor.MODE_RGB_RAW
    print('%i %i %i' % (color_sensor.red, color_sensor.green, color_sensor.blue))

    color_sensor.mode = color_sensor.MODE_COL_COLOR
    print(color_scan_dict[color_sensor.value()])
    sleep(2.5)








