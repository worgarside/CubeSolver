from position_generator import generate_positions
import time
from cube.moves import *
from cube.cube_class import Cube
import datetime

GROUP_THREE = [MOVE.U2, MOVE.D2, MOVE.L2, MOVE.R2, MOVE.F2, MOVE.B2]
GROUP_TWO = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F2, MOVE.B2]
GROUP_ONE = [MOVE.U2, MOVE.D2, MOVE.L, MOVE.R, MOVE.F, MOVE.B]
GROUP_ZERO = [MOVE.U, MOVE.D, MOVE.L, MOVE.R, MOVE.F, MOVE.B]

start = int(round(time.time() * 1000))
pos_vals = generate_positions(Cube(), GROUP_THREE)
end = int(round(time.time() * 1000))

total = (end - start)/1000
print("Total Time: " + str(total))

with open(datetime.datetime.now().strftime("%Y-%m-%d %H%M") + ".csv", "w+") as f:
    for p in pos_vals:
        print(len(p))
        for q in p:
            f.write(str(q) + ',')
        f.write("\n")
f.close()
