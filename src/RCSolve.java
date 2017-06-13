import java.awt.Dimension;
import java.awt.Toolkit;
public class RCSolve {
    enum Direction{TOP, BOTTOM, LEFT, RIGHT, FRONT, BACK};
    public static  Cube rubiksCube = solvedCube();

    public static void main(String[] args) {
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension screen = toolkit.getScreenSize();
        CubeGUI inputWindow = new CubeGUI();
        inputWindow.setLocation((screen.width - inputWindow.getWidth()) / 2, (screen.height - inputWindow.getHeight()) / 2);
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