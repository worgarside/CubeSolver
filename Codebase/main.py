from cube.cube_class import Cube
from cube.move_class import Move as MOVE
from position_generator import *
from linked_list import LinkedList

GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

GROUP_TEST = [MOVE.U, MOVE.D]

r_cube = Cube()

generate_positions(Cube(), GROUP_TEST)

l = LinkedList()

l.add( 'a' )
l.add( 'b' )
l.add( 'c' )

print(l)
l.remove( l.search( 'b' ) )
print(l)
