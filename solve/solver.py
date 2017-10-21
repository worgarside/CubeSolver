import solve.ida_star as ida

up = [0, 1, 2, 3, 4, 5, 6, 7, 8]
down = [45, 46, 47, 48, 49, 50, 51, 52, 53]
left = [9, 10, 11, 21, 22, 23, 33, 34, 35]
right = [15, 16, 17, 27, 28, 29, 39, 40, 41]
front = [12, 13, 14, 24, 25, 26, 36, 37, 38]
back = [18, 19, 20, 30, 31, 32, 42, 43, 44]


def solve():
    ida.setup()
    return []
    # return ['l2', 'not_r', 'b', 'not_u', 'not_r', 'b2', 'd', 'r2', 'd2', 'not_l', 'not_d', 'not_u']

"""
    SCRAMBLE = ['u', 'd', 'l', 'd2', 'r2', 'not_d', 'b2', 'r', 'u', 'not_b', 'r', 'l2']

    WBR
    YWY
    BOB
    GBRYBYOGBWRO
    


"""

