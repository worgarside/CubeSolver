import data
from copy import deepcopy
from moves import digital_moves as dmove

def setup():
    cube = deepcopy(data.SOLVED_CUBE)
    for move in data.SIMPLE_SCRAMBLE:
        method = getattr(dmove, move)
        method(cube)

def solve():
    goal_cube = deepcopy(data.SOLVED_CUBE)

    for move in data.SEARCH_MOVES:
        pass
