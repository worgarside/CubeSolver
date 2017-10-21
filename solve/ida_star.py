import data
from copy import deepcopy
from moves import digital_moves as dmove

def setup():
    goal_cube = deepcopy(data.SOLVED_CUBE)
    cube = deepcopy(data.SOLVED_CUBE)
    for move in data.SCRAMBLE:
        method = getattr(dmove, move)
        method(cube)

#
# th = ['u', 'd', 'l', 'd2', 'r2', 'not_d', 'b2', 'r', 'u', 'not_b', 'r', 'l2']
#
