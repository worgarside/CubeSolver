public class SolveImp {
    public static void main(String[] args) {
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension screen = toolkit.getScreenSize();
        CubeGUI inputWindow = new CubeGUI();
        inputWindow.setLocation((screen.width - inputWindow.getWidth()) / 2, (screen.height - inputWindow.getHeight()) / 2);
    }
}