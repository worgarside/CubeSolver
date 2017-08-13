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