public class Solver {
    public static void main(String[] args) {
        createCube();
        displayCube();
//        displaySide(left);
    }

    public static void createCube() {
        Side top = new Side('W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W');
        Side bottom = new Side('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'O');
        Side left = new Side('O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O');
        Side right = new Side('R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R');
        Side front = new Side('G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G');
        Side back = new Side('B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B');

        Cube rubiksCube = new Cube(top, bottom, left, right, front, back);
    }
}