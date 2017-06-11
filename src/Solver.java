import java.io.Console;
public class Solver {
    enum Direction{TOP, BOTTOM, LEFT, RIGHT, FRONT, BACK};

    public static void main(String[] args) {
        Cube rubiksCube = solvedCube();

//        String[] moveChain = {"NotL", "F", "D", "S", "S", "L2", "D2", "M", "NotR", "F", "E2", "S", "NotB", "U", "B2"};
//        String[] moveChain2 = {"F", "U", "D2", "NotR", "F", "L", "L", "L", "L"};
//        String[] moveChain3 = {"NotF", "NotU", "D2", "R", "NotF", "NotL", "NotL", "NotL", "NotL"};
//        rubiksCube.followMoveChain(moveChain3);
    }

    public static Cube solvedCube() {
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