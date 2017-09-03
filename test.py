# face = 3
# change = 0
#
# dict = {
#     0 : change = change + 1,
#     1 : change = change + 2,
#     2 : change = change + 3,
#     3 : change = change + 4,
#     4 : change = change + 5,
#     5 : change = change + 6,
# }
#
# print(dict[face])

from enum import Enum

# Side = Enum("Side", "top bottom left right front back")
#
# side1 = Side.top
# side2 = Side.top
#
# if side1 == side2:
#     print(Side.top)
# else:
#     # print("False")
#     print(side1)


class Side(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3
    FRONT = 4
    BACK = 5

if Side.TOP == 0:
    print(Side.TOP)
else:
    print("fail")
    if True:
        if True:
            print()

# :1:2:3:4:5:6:7:8:9:1:2:3:4:5:6:9#

"""
       Y B W
       R G O
       R G G
 O W Y B Y Y R Y O G W G
 G O G O Y Y R R B O W R
 R Y R G R B W W B O W B
       W B O
       B B O
       W G Y

       Y B W
       R G O
       R G G
 O W Y B Y Y R Y O G W G
 G O G O Y Y R R B O W R
 R Y R G R B W W B O W B
       W B O
       B B O
       W G Y

RIGHT CLOCKWISE
LEFT ccw
down *2

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|######################################################| 100.00%

SOLVED_POS = [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE,
 Color.WHITE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE,
  Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED,
   Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN,
    Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE,
     Color.ORANGE, Color.ORANGE, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW,
      Color.YELLOW, Color.YELLOW, Color.YELLOW]


[(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE),
 (Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN),
 (Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW,
  Color.YELLOW),
 (Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE),
 (Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED),
 (Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE,
  Color.ORANGE)]


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
["x", "r", "u2", "d", "not_z", "not_b", "not_f", "not_f", "r2", "d", "not_x", "not_s", "l2", "y", "not_r", "not_f", "m"]

 
       R W B 
       Y W R 
       W W B 
 W R O G G G Y G Y O R B 
 W B B R O G O G B Y R B 
 R G R R Y O B B Y O W W 
       G O W 
       Y Y O 
       Y O G
       
       R W B 
       Y W R 
       W W B 
 W R O G G G Y G Y O R B 
 W B B R O G O G B Y R B 
 R G R R Y O B B Y O W W 
       G O W 
       Y Y O 
       Y O G


       R W B 
       Y W R 
       W W B 
 W R O G G G Y G Y O R W 
 W B B R O G O G B Y R B 
 R G R R Y O B B Y O W B 
       G O W 
       Y Y O 
       Y O G








new_pos = rubiks_bot.grabber.position - 90
        rubiks_bot.grabber.run_to_abs_pos(position_sp=new_pos, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(new_pos)

        rubiks_bot.grabber.run_to_abs_pos(position_sp=0, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(0)

        sleep(2)
        new_pos = rubiks_bot.grabber.position - 90
        rubiks_bot.grabber.run_to_abs_pos(position_sp=new_pos, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(new_pos)

        rubiks_bot.grabber.run_to_abs_pos(position_sp=0, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(0)

        sleep(2)
        new_pos = rubiks_bot.grabber.position - 90
        rubiks_bot.grabber.run_to_abs_pos(position_sp=new_pos, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(new_pos)

        rubiks_bot.grabber.run_to_abs_pos(position_sp=0, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(0)

        sleep(2)
        new_pos = rubiks_bot.grabber.position - 90
        rubiks_bot.grabber.run_to_abs_pos(position_sp=new_pos, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(new_pos)

        rubiks_bot.grabber.run_to_abs_pos(position_sp=0, speed_sp=rubiks_bot.grabber_speed)
        rubiks_bot.grabber.wait_for_position(0)

        sleep(2)
        
        ##############################################################
        
"u": ["x x d"],
"not_u": ["x x not_d"],
"u2": ["x x d d"],
"d": ["d"],
"not_d": ["not_d"],
"d2": ["d d"],
"l": ["y x d"],
"not_l": ["y x not_d"],
"l2": ["y x d d"],
"r": ["not_y x d"],
"not_r": ["not_y x not_d"],
"r2": ["not_y x d d"],
"f": ["x x x d"],
"not_f": ["x x x not_d"],
"f2": ["x x x d d"],
"b": ["x d"],
"not_b": ["x not_d"],
"b2": ["x d d"],
"m": ["y x not_d x x d"],
"not_m": ["y x d x x not_d"],
"m2": ["y x d d x x not_d not_d"],
"e": ["not_d x x d"],
"not_e": ["d x x not_d"],
"e2": ["d d x x not_d not_d"],
"s": ["y y x not_d x x d"],
"not_s": ["y y x d x x not_d"],
"s2": ["y y x d d x x not_d not_d"],
"x": ["x"],
"not_x": ["x x x"],
"x2": ["x x"],
"y": ["y"],
"not_y": ["not_y"],
"y2": ["y y"],
"z": ["not_y x"],
"not_z": ["y x"],
"z2": ["y x x not_y"]
        
        
        
        
"""
