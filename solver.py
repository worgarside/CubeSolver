from color_class import Color
from enum import Enum
import data

up = [0, 1, 2, 3, 4, 5, 6, 7, 8]
down = [45, 46, 47, 48, 49, 50, 51, 52, 53]
left = [9, 10, 11, 21, 22, 23, 33, 34, 35]
right = [15, 16, 17, 27, 28, 29, 39, 40, 41]
front = [12, 13, 14, 24, 25, 26, 36, 37, 38]
back = [18, 19, 20, 30, 31, 32, 42, 43, 44]


class CubieType(Enum):
    MIDDLES = [1, 3, 5, 7, 10, 13, 16, 19, 21, 23, 24, 26, 27, 29, 30, 32, 34, 37, 40, 43, 46, 48, 50, 52]
    CORNERS = [0, 2, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 51, 53]
    CENTRES = [4, 22, 25, 28, 29, 31, 49]


def solve(self):
    white_cross(self)

    return ['d2', 'e', 'r2', 'e2', 's2', 'u', 'm']


def get_color_by_cubie_type(self, color, cubie_type=None):
    type_list = []
    for index, cubie in enumerate(self._pos):
        if cubie == color:
            if cubie_type is None:
                type_list.append(index)
            else:
                for ct in CubieType:
                    if (cubie_type == ct) and index in ct.value:
                        type_list.append(index)
    return type_list


def get_cubies_by_type_and_side(cubie_type, side):
    return list(set(eval(side.name.lower())).intersection(cubie_type.value))


def white_cross(self):
    white_middles = get_color_by_cubie_type(self, Color.WHITE, CubieType.MIDDLES)
    print(white_middles)

    # while white_middles != get_cubies_by_type_and_side(CubieType.MIDDLES, self._white_side):
    #     pass

    # move any white middles from sides to yellow face - unless they're in correct place already
