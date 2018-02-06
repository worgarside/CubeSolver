from linked_list import LinkedList
from cube.move_class import Move as MOVE
import datetime

def generate_positions(cube, group):
    depth = 0
    id = 0
    pos_list = LinkedList()
    with open(datetime.datetime.now().strftime("%Y-%m-%d %H%M") + ".csv", "w+") as f:
        while depth < 500000:
            pos_list.push(id, cube.pos, MOVE.U, depth)
            depth += 1
            print(depth, end=' ')
            f.write(str(id) + ',' + cube.pos + ',' + str(MOVE.U) + ',' + str(depth) + "\n")
    f.close()
    # print(pos_list)
