from cube.cube_class import Cube
from cube.moves import *
import datetime
positions = set()

def generate_positions(cube, group):
    # with open(datetime.datetime.now().strftime("%Y-%m-%d %H%M") + ".csv", "w+") as f:
    #     f.write("pos_id, pos, parent_id, parent_move, final\n")
    #     f.write("0, " + cube.cube_class.Cube().pos+ ", -1, -, 0\n")
    #
    #     c = deepcopy(cube)
    #     current_id = 1
    #     for i in range(4):
    #         u(c)
    #         if c.pos not in positions:
    #             this_id = current_id + 1
    #             positions.add(c.pos)
    #             entry = str(this_id) + ", " + c.pos + ", " + str(current_id) + ", ??, 0\n"
    #             f.write(entry)
    #
    #     f.close()
    pass