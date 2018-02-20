from enum import Enum, unique

@unique
class Move(Enum):
    NONE = '-'
    U = 'U '
    NOT_U = "U'"
    U2 = 'U2'
    D = 'D '
    NOT_D = "D'"
    D2 ='D2'
    L = 'L '
    NOT_L = "L'"
    L2 ='L2'
    R = 'R '
    NOT_R = "R'"
    R2 = 'R2'
    F = 'F '
    NOT_F = "F'"
    F2 = 'F2'
    B = 'B '
    NOT_B = "B'"
    B2 = 'B2'
    M = 'M '
    NOT_M = "M'"
    M2 = 'M2'
    E = 'E '
    NOT_E = "E'"
    E2 = 'E2'
    S = 'S '
    NOT_S = "S'"
    S2 = 'S2'
    X = 'X '
    NOT_X = "X'"
    X2 = 'X2'
    Y = 'Y '
    NOT_Y = "Y'"
    Y2 = 'Y2'
    Z = 'Z '
    NOT_Z = "Z'"
    Z2 = 'Z2'
