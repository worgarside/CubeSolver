from enum import Enum, unique

@unique
class Side(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    FRONT = 'F'
    BACK = 'B'
