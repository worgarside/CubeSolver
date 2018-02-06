from cube.cube_class import Cube
from cube.move_class import Move as MOVE
from position_generator import *
from linked_list import LinkedList

# GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
# GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
# GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
# GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
#
# GROUP_TEST = [MOVE.U, MOVE.D]
#
# r_cube = Cube()
#
# generate_positions(Cube(), GROUP_TEST)

l = LinkedList()

l.push(1, 'WYORGB', MOVE.U, False)
l.push(2, 'ORGBWY', MOVE.U, False)
l.push(3, 'GBWYOR', MOVE.U, False)
l.push(4, 'BGROYW', MOVE.U, False)
l.push(5, 'WWWWWW', MOVE.U, True)

print(l)
