from enum import Enum, unique

@unique
class Color(Enum):
    """An Enum Class to hold potential colors scanned by the LEGO Color Sensor"""

    NONE = 'N'
    DARK = 'D'  # DARK (not 'BLACK') to show up with any color reading errors (differentiates it from BLUE)
    BLUE = 'B'
    GREEN = 'G'
    YELLOW = 'Y'
    RED = 'R'
    WHITE = 'W'
    ORANGE = 'O'  # Color Sensor actually reads BROWN but ORANGE is used to avoid confusion
