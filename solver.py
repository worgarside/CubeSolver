from color_class import Color
from enum import Enum


class Location(Enum):
    MIDDLES = [1, 3, 5, 7, 10, 13, 16, 19, 21, 23, 24, 26, 27, 29, 30, 32, 34, 37, 40, 43, 46, 48, 50, 52]
    CORNERS = [0, 2, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 51, 53]
    CENTRES = [4, 22, 25, 28, 29, 31, 49]


def solve(self):
    white_cross(self)


def get_color_by_location(self, color, location=None):
    location_list = []
    for index, cubie in enumerate(self._pos):
        if cubie == color:
            if location == None:
                location_list.append(index)
            else:
                for l in Location:
                    if (location == l) and index in l.value:
                        location_list.append(index)
    return location_list


def white_cross(self):
    white_middles = get_color_by_location(self, Color.WHITE, Location.MIDDLES)

    print(white_middles)
