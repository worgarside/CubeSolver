from position_generator import *
import time

GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

GROUP_TEST = [MOVE.U, MOVE.R]
#
# r_cube = Cube()
#
start = int(round(time.time() * 1000))
generate_positions(Cube(), GROUP_THREE)
end = int(round(time.time() * 1000))

total = (end - start)/1000
print("Total Time: " + str(total))
# l = LinkedList()
#
# l.push(1, 'WYORGB', MOVE.U, 1, False)
# l.push(2, 'ORGBWY', MOVE.U, 2, False)
# l.push(3, 'GBWYOR', MOVE.U, 2, False)
# l.push(4, 'BGROYW', MOVE.U, 3, False)
# l.push(5, 'WWWWWW', MOVE.U, 3, True)
#
# print(l)
