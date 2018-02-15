from enum import Enum


class Color(Enum):
    """An Enum Class to hold potential colors scanned by the LEGO Color Sensor"""

    NONE = 0
    DARK = 1  # DARK (not 'BLACK') to show up with any color reading errors (differentiates it from BLUE)
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5
    WHITE = 6
    ORANGE = 7  # Color Sensor actually reads BROWN
