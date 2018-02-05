from cube.cube_class import Cube
import cube.moves as move

r_cube = Cube()

move.d2(r_cube)
move.b(r_cube)
move.not_u(r_cube)
move.l(r_cube)
move.not_d(r_cube)
move.f(r_cube)
move.b2(r_cube)
move.not_d(r_cube)
move.b(r_cube)
move.not_f(r_cube)
move.not_f(r_cube)
move.u(r_cube)
move.not_r(r_cube)
move.u(r_cube)

print(r_cube)