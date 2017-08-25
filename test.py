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

SOLVED_POS = [Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW]


[(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE),
 (Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN),
 (Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW),
 (Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE),
 (Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED),
 (Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE, Color.ORANGE)]














"""



