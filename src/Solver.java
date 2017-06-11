public class Solver {
    enum Direction{TOP, BOTTOM, LEFT, RIGHT, FRONT, BACK};

    public static void main(String[] args) {
        Cube rubiksCube = newCube();
        System.out.println(rubiksCube);
        System.out.println("-------------------------------------------------------- \n");

//        rubiksCube.moveR();
//        rubiksCube.moveNotR();
//        rubiksCube.moveL();
//        rubiksCube.moveNotL();
//        rubiksCube.moveR2();
//        rubiksCube.moveL2();
//        rubiksCube.moveU();
//        rubiksCube.moveNotU();
//        rubiksCube.moveD();
//        rubiksCube.moveNotD();
//        rubiksCube.moveU2();
//        rubiksCube.moveD2();
//        rubiksCube.moveF();
//        rubiksCube.moveNotF();
//        rubiksCube.moveB();
//        rubiksCube.moveNotB();
//        rubiksCube.moveF2();
//        rubiksCube.moveB2();
//        rubiksCube.moveM();
//        rubiksCube.moveNotM();
//        rubiksCube.moveM2();
//        rubiksCube.moveE();
//        rubiksCube.moveNotE();
//        rubiksCube.moveE2();
//        rubiksCube.moveS();
//        rubiksCube.moveNotS();
//        rubiksCube.moveS2();
//        rubiksCube.moveX();
//        rubiksCube.moveNotX();
//        rubiksCube.moveY();
//        rubiksCube.moveNotY();
//        rubiksCube.moveZ();
//        rubiksCube.moveNotZ();
        System.out.println(rubiksCube);
        System.out.println("---------------------------------------------------------- \n");








    }

    public static Cube newCube() {
        Side top = new Side('W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W');
        Side bottom = new Side('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y');
        Side left = new Side('O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O');
        Side right = new Side('R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R');
        Side front = new Side('G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G');
        Side back = new Side('B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B');

        Cube tempCube = new Cube(top, bottom, left, right, front, back);

        return tempCube;
    }
}