from cube.move_class import Move as MOVE


def dyn_move(move, print_flag=False):
    move_dict = {
        MOVE.U: 'u',
        MOVE.NOT_U: 'not_u',
        MOVE.U2: 'u2',
        MOVE.D: 'd',
        MOVE.NOT_D: 'not_d',
        MOVE.D2: 'd2',
        MOVE.L: 'l',
        MOVE.NOT_L: 'not_l',
        MOVE.L2: 'l2',
        MOVE.R: 'r',
        MOVE.NOT_R: 'not_r',
        MOVE.R2: 'r2',
        MOVE.F: 'f',
        MOVE.NOT_F: 'not_f',
        MOVE.F2: 'f2',
        MOVE.B: 'b',
        MOVE.NOT_B: 'not_b',
        MOVE.B2: 'b2',
        MOVE.M: 'm',
        MOVE.NOT_M: 'not_m',
        MOVE.M2: 'm2',
        MOVE.E: 'e',
        MOVE.NOT_E: 'not_e',
        MOVE.E2: 'e2',
        MOVE.S: 's',
        MOVE.NOT_S: 'not_s',
        MOVE.S2: 's2',
        MOVE.X: 'x',
        MOVE.NOT_X: 'not_x',
        MOVE.X2: 'x2',
        MOVE.Y: 'y',
        MOVE.NOT_Y: 'not_y',
        MOVE.Y2: 'y2',
        MOVE.Z: 'z',
        MOVE.NOT_Z: 'not_z',
        MOVE.Z2: 'z2'
    }

    return move_dict[move]

print(MOVE.Z.value)
dyn_move('Z')

