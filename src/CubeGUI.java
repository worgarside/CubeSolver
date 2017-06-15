import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.*;
import javax.swing.*;
import java.awt.Color;
import java.awt.Font;
import java.util.Random;

@SuppressWarnings("serial")
public class CubeGUI extends JFrame {
    final int WIDTH = 1080;
    final int HEIGHT = 720;

    final int BTN_COL1 = 715;
    final int BTN_COL2 = 775;
    final int BTN_COL3 = 835;
    final int BTN_COL4 = 895;
    final int BTN_COL5 = 955;
    final int BTN_COL6 = 1015;

    final int BTN_ROW1 = 200;
    final int BTN_ROW2 = 250;
    final int BTN_ROW3 = 300;
    final int BTN_ROW4 = 350;
    final int BTN_ROW5 = 400;
    final int BTN_ROW6 = 450;
    final int BTN_ROW7 = 500;

    private Timer randomMoveTimer;
    private int rnd, moveCount;

    JPanel topNorthWest = new JPanel();
    JPanel topNorth = new JPanel();
    JPanel topNorthEast = new JPanel();
    JPanel topWest = new JPanel();
    JPanel topCentre = new JPanel();
    JPanel topEast = new JPanel();
    JPanel topSouthWest = new JPanel();
    JPanel topSouth = new JPanel();
    JPanel topSouthEast = new JPanel();
    JPanel bottomNorthWest = new JPanel();
    JPanel bottomNorth = new JPanel();
    JPanel bottomNorthEast = new JPanel();
    JPanel bottomWest = new JPanel();
    JPanel bottomCentre = new JPanel();
    JPanel bottomEast = new JPanel();
    JPanel bottomSouthWest = new JPanel();
    JPanel bottomSouth = new JPanel();
    JPanel bottomSouthEast = new JPanel();
    JPanel leftNorthWest = new JPanel();
    JPanel leftNorth = new JPanel();
    JPanel leftNorthEast = new JPanel();
    JPanel leftWest = new JPanel();
    JPanel leftCentre = new JPanel();
    JPanel leftEast = new JPanel();
    JPanel leftSouthWest = new JPanel();
    JPanel leftSouth = new JPanel();
    JPanel leftSouthEast = new JPanel();
    JPanel rightNorthWest = new JPanel();
    JPanel rightNorth = new JPanel();
    JPanel rightNorthEast = new JPanel();
    JPanel rightWest = new JPanel();
    JPanel rightCentre = new JPanel();
    JPanel rightEast = new JPanel();
    JPanel rightSouthWest = new JPanel();
    JPanel rightSouth = new JPanel();
    JPanel rightSouthEast = new JPanel();
    JPanel frontNorthWest = new JPanel();
    JPanel frontNorth = new JPanel();
    JPanel frontNorthEast = new JPanel();
    JPanel frontWest = new JPanel();
    JPanel frontCentre = new JPanel();
    JPanel frontEast = new JPanel();
    JPanel frontSouthWest = new JPanel();
    JPanel frontSouth = new JPanel();
    JPanel frontSouthEast = new JPanel();
    JPanel backNorthWest = new JPanel();
    JPanel backNorth = new JPanel();
    JPanel backNorthEast = new JPanel();
    JPanel backWest = new JPanel();
    JPanel backCentre = new JPanel();
    JPanel backEast = new JPanel();
    JPanel backSouthWest = new JPanel();
    JPanel backSouth = new JPanel();
    JPanel backSouthEast = new JPanel();

    public CubeGUI() {
        randomMoveTimer = new Timer(250, new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                if(moveCount < rnd){
                    int moveNum = new Random().nextInt(Cube.MOVES.length);
                    String move = Cube.MOVES[moveNum];
                    RCSolveMain.rubiksCube.move(move);
                    updateCubeNet();
                    moveCount ++;
                }else{
                    randomMoveTimer.stop();
                    System.out.println();
                }
            }
        });

        java.awt.Container contentPane = getContentPane();
        setTitle("Rubik's Cube Solver");
        setSize(WIDTH, HEIGHT);
        setResizable(false);
        setLayout(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel cubeNetPanel = new JPanel(); // Holds the buttons
        cubeNetPanel.setBackground(Color.GRAY);
        cubeNetPanel.setBounds(70, 100, 630, 480);

        //******** TOP SIDE ********\\

        topNorthWest.setBackground(Color.WHITE);
        topNorthWest.setBounds(240, 120, 40, 40);
        topNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topNorthWest);

        topNorth.setBackground(Color.WHITE);
        topNorth.setBounds(290, 120, 40, 40);
        topNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topNorth);

        topNorthEast.setBackground(Color.WHITE);
        topNorthEast.setBounds(340, 120, 40, 40);
        topNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topNorthEast);

        topWest.setBackground(Color.WHITE);
        topWest.setBounds(240, 170, 40, 40);
        topWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topWest);

        topCentre.setBackground(Color.WHITE);
        topCentre.setBounds(290, 170, 40, 40);
        topCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topCentre);

        topEast.setBackground(Color.WHITE);
        topEast.setBounds(340, 170, 40, 40);
        topEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topEast);

        topSouthWest.setBackground(Color.WHITE);
        topSouthWest.setBounds(240, 220, 40, 40);
        topSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topSouthWest);

        topSouth.setBackground(Color.WHITE);
        topSouth.setBounds(290, 220, 40, 40);
        topSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topSouth);

        topSouthEast.setBackground(Color.WHITE);
        topSouthEast.setBounds(340, 220, 40, 40);
        topSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topSouthEast);

        //******** BOTTOM SIDE ********\\

        bottomNorthWest.setBackground(Color.YELLOW);
        bottomNorthWest.setBounds(240, 420, 40, 40);
        bottomNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomNorthWest);

        bottomNorth.setBackground(Color.YELLOW);
        bottomNorth.setBounds(290, 420, 40, 40);
        bottomNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomNorth);

        bottomNorthEast.setBackground(Color.YELLOW);
        bottomNorthEast.setBounds(340, 420, 40, 40);
        bottomNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomNorthEast);

        bottomWest.setBackground(Color.YELLOW);
        bottomWest.setBounds(240, 470, 40, 40);
        bottomWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomWest);

        bottomCentre.setBackground(Color.YELLOW);
        bottomCentre.setBounds(290, 470, 40, 40);
        bottomCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomCentre);

        bottomEast.setBackground(Color.YELLOW);
        bottomEast.setBounds(340, 470, 40, 40);
        bottomEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomEast);

        bottomSouthWest.setBackground(Color.YELLOW);
        bottomSouthWest.setBounds(240, 520, 40, 40);
        bottomSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomSouthWest);

        bottomSouth.setBackground(Color.YELLOW);
        bottomSouth.setBounds(290, 520, 40, 40);
        bottomSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomSouth);

        bottomSouthEast.setBackground(Color.YELLOW);
        bottomSouthEast.setBounds(340, 520, 40, 40);
        bottomSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomSouthEast);

        //******** LEFT SIDE ********\\

        leftNorthWest.setBackground(new Color(255, 153, 0));
        leftNorthWest.setBounds(90, 270, 40, 40);
        leftNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftNorthWest);

        leftNorth.setBackground(new Color(255, 153, 0));
        leftNorth.setBounds(140, 270, 40, 40);
        leftNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftNorth);

        leftNorthEast.setBackground(new Color(255, 153, 0));
        leftNorthEast.setBounds(190, 270, 40, 40);
        leftNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftNorthEast);

        leftWest.setBackground(new Color(255, 153, 0));
        leftWest.setBounds(90, 320, 40, 40);
        leftWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftWest);

        leftCentre.setBackground(new Color(255, 153, 0));
        leftCentre.setBounds(140, 320, 40, 40);
        leftCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftCentre);

        leftEast.setBackground(new Color(255, 153, 0));
        leftEast.setBounds(190, 320, 40, 40);
        leftEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftEast);

        leftSouthWest.setBackground(new Color(255, 153, 0));
        leftSouthWest.setBounds(90, 370, 40, 40);
        leftSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftSouthWest);

        leftSouth.setBackground(new Color(255, 153, 0));
        leftSouth.setBounds(140, 370, 40, 40);
        leftSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftSouth);

        leftSouthEast.setBackground(new Color(255, 153, 0));
        leftSouthEast.setBounds(190, 370, 40, 40);
        leftSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftSouthEast);

        //******** RIGHT SIDE ********\\

        rightNorthWest.setBackground(Color.RED);
        rightNorthWest.setBounds(390, 270, 40, 40);
        rightNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightNorthWest);

        rightNorth.setBackground(Color.RED);
        rightNorth.setBounds(440, 270, 40, 40);
        rightNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightNorth);

        rightNorthEast.setBackground(Color.RED);
        rightNorthEast.setBounds(490, 270, 40, 40);
        rightNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightNorthEast);

        rightWest.setBackground(Color.RED);
        rightWest.setBounds(390, 320, 40, 40);
        rightWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightWest);

        rightCentre.setBackground(Color.RED);
        rightCentre.setBounds(440, 320, 40, 40);
        rightCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightCentre);

        rightEast.setBackground(Color.RED);
        rightEast.setBounds(490, 320, 40, 40);
        rightEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightEast);

        rightSouthWest.setBackground(Color.RED);
        rightSouthWest.setBounds(390, 370, 40, 40);
        rightSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightSouthWest);

        rightSouth.setBackground(Color.RED);
        rightSouth.setBounds(440, 370, 40, 40);
        rightSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightSouth);

        rightSouthEast.setBackground(Color.RED);
        rightSouthEast.setBounds(490, 370, 40, 40);
        rightSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightSouthEast);

        //******** FRONT SIDE ********\\

        frontNorthWest.setBackground(Color.GREEN);
        frontNorthWest.setBounds(240, 270, 40, 40);
        frontNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontNorthWest);

        frontNorth.setBackground(Color.GREEN);
        frontNorth.setBounds(290, 270, 40, 40);
        frontNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontNorth);

        frontNorthEast.setBackground(Color.GREEN);
        frontNorthEast.setBounds(340, 270, 40, 40);
        frontNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontNorthEast);

        frontWest.setBackground(Color.GREEN);
        frontWest.setBounds(240, 320, 40, 40);
        frontWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontWest);

        frontCentre.setBackground(Color.GREEN);
        frontCentre.setBounds(290, 320, 40, 40);
        frontCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontCentre);

        frontEast.setBackground(Color.GREEN);
        frontEast.setBounds(340, 320, 40, 40);
        frontEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontEast);

        frontSouthWest.setBackground(Color.GREEN);
        frontSouthWest.setBounds(240, 370, 40, 40);
        frontSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontSouthWest);

        frontSouth.setBackground(Color.GREEN);
        frontSouth.setBounds(290, 370, 40, 40);
        frontSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontSouth);

        frontSouthEast.setBackground(Color.GREEN);
        frontSouthEast.setBounds(340, 370, 40, 40);
        frontSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontSouthEast);

        //******** BACK SIDE ********\\

        backNorthWest.setBackground(Color.BLUE);
        backNorthWest.setBounds(540, 270, 40, 40);
        backNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backNorthWest);

        backNorth.setBackground(Color.BLUE);
        backNorth.setBounds(590, 270, 40, 40);
        backNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backNorth);

        backNorthEast.setBackground(Color.BLUE);
        backNorthEast.setBounds(640, 270, 40, 40);
        backNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backNorthEast);

        backWest.setBackground(Color.BLUE);
        backWest.setBounds(540, 320, 40, 40);
        backWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backWest);

        backCentre.setBackground(Color.BLUE);
        backCentre.setBounds(590, 320, 40, 40);
        backCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backCentre);

        backEast.setBackground(Color.BLUE);
        backEast.setBounds(640, 320, 40, 40);
        backEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backEast);

        backSouthWest.setBackground(Color.BLUE);
        backSouthWest.setBounds(540, 370, 40, 40);
        backSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backSouthWest);

        backSouth.setBackground(Color.BLUE);
        backSouth.setBounds(590, 370, 40, 40);
        backSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backSouth);

        backSouthEast.setBackground(Color.BLUE);
        backSouthEast.setBounds(640, 370, 40, 40);
        backSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backSouthEast);


        //******** MOVE BUTTONS ********\\

        JButton btnMoveL = new JButton("L");
        btnMoveL.setBounds(BTN_COL1, BTN_ROW1, 50, 30);
        btnMoveL.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveL();
                //System.out.print("L, ");

            }
        });
        contentPane.add(btnMoveL);

        JButton btnMoveNotL = new JButton("L'");
        btnMoveNotL.setBounds(BTN_COL2, BTN_ROW1, 50, 30);
        btnMoveNotL.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotL();
                //System.out.print("NotL, ");

            }
        });
        contentPane.add(btnMoveNotL);

        JButton btnMoveL2 = new JButton("L2");
        btnMoveL2.setBounds(BTN_COL3, BTN_ROW1, 50, 30);
        btnMoveL2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveL2();
            }
        });
        contentPane.add(btnMoveL2);

        JButton btnMoveR = new JButton("R");
        btnMoveR.setBounds(BTN_COL4, BTN_ROW1, 50, 30);
        btnMoveR.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveR();
            }
        });
        contentPane.add(btnMoveR);

        JButton btnMoveNotR = new JButton("R'");
        btnMoveNotR.setBounds(BTN_COL5, BTN_ROW1, 50, 30);
        btnMoveNotR.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotR();
            }
        });
        contentPane.add(btnMoveNotR);

        JButton btnMoveR2 = new JButton("R2");
        btnMoveR2.setBounds(BTN_COL6, BTN_ROW1, 50, 30);
        btnMoveR2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveR2();
            }
        });
        contentPane.add(btnMoveR2);

        JButton btnMoveU = new JButton("U");
        btnMoveU.setBounds(BTN_COL1, BTN_ROW2, 50, 30);
        btnMoveU.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveU();
            }
        });
        contentPane.add(btnMoveU);

        JButton btnMoveNotU = new JButton("U'");
        btnMoveNotU.setBounds(BTN_COL2, BTN_ROW2, 50, 30);
        btnMoveNotU.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotU();
            }
        });
        contentPane.add(btnMoveNotU);

        JButton btnMoveU2 = new JButton("U2");
        btnMoveU2.setBounds(BTN_COL3, BTN_ROW2, 50, 30);
        btnMoveU2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveU2();
            }
        });
        contentPane.add(btnMoveU2);

        JButton btnMoveD = new JButton("D");
        btnMoveD.setBounds(BTN_COL4, BTN_ROW2, 50, 30);
        btnMoveD.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveD();
            }
        });
        contentPane.add(btnMoveD);

        JButton btnMoveNotD = new JButton("D'");
        btnMoveNotD.setBounds(BTN_COL5, BTN_ROW2, 50, 30);
        btnMoveNotD.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotD();
            }
        });
        contentPane.add(btnMoveNotD);

        JButton btnMoveD2 = new JButton("D2");
        btnMoveD2.setBounds(BTN_COL6, BTN_ROW2, 50, 30);
        btnMoveD2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveD2();
            }
        });
        contentPane.add(btnMoveD2);

        JButton btnMoveF = new JButton("F");
        btnMoveF.setBounds(BTN_COL1, BTN_ROW3, 50, 30);
        btnMoveF.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveF();
            }
        });
        contentPane.add(btnMoveF);

        JButton btnMoveNotF = new JButton("F'");
        btnMoveNotF.setBounds(BTN_COL2, BTN_ROW3, 50, 30);
        btnMoveNotF.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotF();
            }
        });
        contentPane.add(btnMoveNotF);

        JButton btnMoveF2 = new JButton("F2");
        btnMoveF2.setBounds(BTN_COL3, BTN_ROW3, 50, 30);
        btnMoveF2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveF2();
            }
        });
        contentPane.add(btnMoveF2);

        JButton btnMoveB = new JButton("B");
        btnMoveB.setBounds(BTN_COL4, BTN_ROW3, 50, 30);
        btnMoveB.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveB();
            }
        });
        contentPane.add(btnMoveB);

        JButton btnMoveNotB = new JButton("B'");
        btnMoveNotB.setBounds(BTN_COL5, BTN_ROW3, 50, 30);
        btnMoveNotB.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotB();
            }
        });
        contentPane.add(btnMoveNotB);

        JButton btnMoveB2 = new JButton("B2");
        btnMoveB2.setBounds(BTN_COL6, BTN_ROW3, 50, 30);
        btnMoveB2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveB2();
            }
        });
        contentPane.add(btnMoveB2);

        JButton btnMoveM = new JButton("M");
        btnMoveM.setBounds(BTN_COL1, BTN_ROW4, 50, 30);
        btnMoveM.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveM();
            }
        });
        contentPane.add(btnMoveM);

        JButton btnMoveNotM = new JButton("M'");
        btnMoveNotM.setBounds(BTN_COL2, BTN_ROW4, 50, 30);
        btnMoveNotM.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotM();
            }
        });
        contentPane.add(btnMoveNotM);

        JButton btnMoveM2 = new JButton("M2");
        btnMoveM2.setBounds(BTN_COL3, BTN_ROW4, 50, 30);
        btnMoveM2.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 11));
        btnMoveM2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveM2();
            }
        });
        contentPane.add(btnMoveM2);

        JButton btnMoveE = new JButton("E");
        btnMoveE.setBounds(BTN_COL4, BTN_ROW4, 50, 30);
        btnMoveE.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveE();
            }
        });
        contentPane.add(btnMoveE);

        JButton btnMoveNotE = new JButton("E'");
        btnMoveNotE.setBounds(BTN_COL5, BTN_ROW4, 50, 30);
        btnMoveNotE.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotE();
            }
        });
        contentPane.add(btnMoveNotE);

        JButton btnMoveE2 = new JButton("E2");
        btnMoveE2.setBounds(BTN_COL6, BTN_ROW4, 50, 30);
        btnMoveE2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveE2();
            }
        });
        contentPane.add(btnMoveE2);

        JButton btnMoveS = new JButton("S");
        btnMoveS.setBounds(BTN_COL1, BTN_ROW5, 50, 30);
        btnMoveS.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveS();
            }
        });
        contentPane.add(btnMoveS);

        JButton btnMoveNotS = new JButton("S'");
        btnMoveNotS.setBounds(BTN_COL2, BTN_ROW5, 50, 30);
        btnMoveNotS.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotS();
            }
        });
        contentPane.add(btnMoveNotS);

        JButton btnMoveS2 = new JButton("S2");
        btnMoveS2.setBounds(BTN_COL3, BTN_ROW5, 50, 30);
        btnMoveS2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveS2();
            }
        });
        contentPane.add(btnMoveS2);

        JButton btnMoveX = new JButton("X");
        btnMoveX.setBounds(BTN_COL1, BTN_ROW6, 50, 30);
        btnMoveX.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveX();
            }
        });
        contentPane.add(btnMoveX);

        JButton btnMoveNotX = new JButton("X'");
        btnMoveNotX.setBounds(BTN_COL2, BTN_ROW6, 50, 30);
        btnMoveNotX.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotX();
            }
        });
        contentPane.add(btnMoveNotX);

        JButton btnMoveX2 = new JButton("X2");
        btnMoveX2.setBounds(BTN_COL3, BTN_ROW6, 50, 30);
        btnMoveX2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveX2();
            }
        });
        contentPane.add(btnMoveX2);

        JButton btnMoveY = new JButton("Y");
        btnMoveY.setBounds(BTN_COL4, BTN_ROW6, 50, 30);
        btnMoveY.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveY();
            }
        });
        contentPane.add(btnMoveY);

        JButton btnMoveNotY = new JButton("Y'");
        btnMoveNotY.setBounds(BTN_COL5, BTN_ROW6, 50, 30);
        btnMoveNotY.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotY();
            }
        });
        contentPane.add(btnMoveNotY);

        JButton btnMoveY2 = new JButton("Y2");
        btnMoveY2.setBounds(BTN_COL6, BTN_ROW6, 50, 30);
        btnMoveY2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveY2();
            }
        });
        contentPane.add(btnMoveY2);

        JButton btnMoveZ = new JButton("Z");
        btnMoveZ.setBounds(BTN_COL1, BTN_ROW7, 50, 30);
        btnMoveZ.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveZ();
            }
        });
        contentPane.add(btnMoveZ);

        JButton btnMoveNotZ = new JButton("Z'");
        btnMoveNotZ.setBounds(BTN_COL2, BTN_ROW7, 50, 30);
        btnMoveNotZ.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveNotZ();
            }
        });
        contentPane.add(btnMoveNotZ);

        JButton btnMoveZ2 = new JButton("Z2");
        btnMoveZ2.setBounds(BTN_COL3, BTN_ROW7, 50, 30);
        btnMoveZ2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.moveZ2();
            }
        });
        contentPane.add(btnMoveZ2);

        contentPane.add(cubeNetPanel);

        JButton btnSolve = new JButton("Solve");
        btnSolve.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.solve();
            }
        });
        btnSolve.setBounds(WIDTH-100, HEIGHT-70, 80, 30);
        contentPane.add(btnSolve);

        JButton btnRandomize = new JButton("Randomize");
        btnRandomize.setBounds(WIDTH-220, HEIGHT-70, 100, 30);
        btnRandomize.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                rnd = 10 + (int)(Math.random() * (11)); //Random int from 10-20
                moveCount = 0;
                System.out.print("\nMaking " + rnd + " moves: ");
                randomMoveTimer.start();
           }
        });
        contentPane.add(btnRandomize);

        JButton btnMoveChain = new JButton("Move Chain");
        btnMoveChain.setBounds(WIDTH-340, HEIGHT-70, 100, 30);
        btnMoveChain.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
//                String[] moveChain = {"M", "S2", "E", "F2", "R", "NotL", "R", "NotR", "L", "S", "NotU", "NotX", "NotU", "NotR", "E", "F", "NotU", "E", "NotR", "NotL", "NotB", "NotL", "S2", "X", "M", "S2", "E", "F2", "R", "NotL", "R", "NotR", "L", "S", "NotU", "NotX", "NotU", "NotR", "E", "F", "NotU", "E", "NotR", "NotL", "NotB", "NotL", "S2", "X"};
//                String[] moveChain = {"NotU", "NotR", "E", "F", "NotU", "E", "NotR", "NotL", "NotB", "NotL", "S2", "X", "M", "S2", "E", "F2", "R", "NotL", "R", "NotR", "L", "S", "NotU"};
                String[] moveChain = {"NotE", "D2", "D2", "NotX", "X", "D2", "E2", "M", "B2", "R2", "NotD", "D2", "U2", "NotS", "NotR", "R2", "L", "NotY", "F2", "NotE"};
                RCSolveMain.rubiksCube.followMoveChain(moveChain);
            }
        });
        contentPane.add(btnMoveChain);

        JButton btnReset = new JButton("Reset");
        btnReset.setBounds(WIDTH-460, HEIGHT-70, 100, 30);
        btnReset.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.reset();
                System.out.println(RCSolveMain.rubiksCube);
                updateCubeNet();
            }
        });
        contentPane.add(btnReset);

        JButton btnAction = new JButton("Action");
        btnAction.setBounds(30, HEIGHT-70, 100, 30);
        btnAction.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                RCSolveMain.rubiksCube.action();
            }
        });
        contentPane.add(btnAction);

        setVisible(true);
    }

    public void updateCubeNet(){
        Color[] colors = new Color[26];
        colors[1] = Color.blue;
        colors[6] = Color.green;
        colors[14] = new Color(255, 153, 0);
        colors[17] = Color.red;
        colors[22] = Color.white;
        colors[24] = Color.yellow;

        topNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getNorthWest()) - 65]);

        topNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getNorthWest() - 65)]);
        topNorth.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getNorth() - 65)]);
        topNorthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getNorthEast() - 65)]);
        topWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getWest() - 65)]);
        topCentre.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getCentre() - 65)]);
        topEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getEast() - 65)]);
        topSouthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getSouthWest() - 65)]);
        topSouth.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getSouth() - 65)]);
        topSouthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getTop().getSouthEast() - 65)]);

        bottomNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getNorthWest() - 65)]);
        bottomNorth.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getNorth() - 65)]);
        bottomNorthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getNorthEast() - 65)]);
        bottomWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getWest() - 65)]);
        bottomCentre.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getCentre() - 65)]);
        bottomEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getEast() - 65)]);
        bottomSouthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getSouthWest() - 65)]);
        bottomSouth.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getSouth() - 65)]);
        bottomSouthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getBottom().getSouthEast() - 65)]);

        leftNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getNorthWest() - 65)]);
        leftNorth.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getNorth() - 65)]);
        leftNorthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getNorthEast() - 65)]);
        leftWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getWest() - 65)]);
        leftCentre.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getCentre() - 65)]);
        leftEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getEast() - 65)]);
        leftSouthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getSouthWest() - 65)]);
        leftSouth.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getSouth() - 65)]);
        leftSouthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getLeft().getSouthEast() - 65)]);

        rightNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getNorthWest() - 65)]);
        rightNorth.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getNorth() - 65)]);
        rightNorthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getNorthEast() - 65)]);
        rightWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getWest() - 65)]);
        rightCentre.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getCentre() - 65)]);
        rightEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getEast() - 65)]);
        rightSouthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getSouthWest() - 65)]);
        rightSouth.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getSouth() - 65)]);
        rightSouthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getRight().getSouthEast() - 65)]);

        frontNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getNorthWest() - 65)]);
        frontNorth.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getNorth() - 65)]);
        frontNorthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getNorthEast() - 65)]);
        frontWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getWest() - 65)]);
        frontCentre.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getCentre() - 65)]);
        frontEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getEast() - 65)]);
        frontSouthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getSouthWest() - 65)]);
        frontSouth.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getSouth() - 65)]);
        frontSouthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getFront().getSouthEast() - 65)]);

        backNorthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getNorthWest() - 65)]);
        backNorth.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getNorth() - 65)]);
        backNorthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getNorthEast() - 65)]);
        backWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getWest() - 65)]);
        backCentre.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getCentre() - 65)]);
        backEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getEast() - 65)]);
        backSouthWest.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getSouthWest() - 65)]);
        backSouth.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getSouth() - 65)]);
        backSouthEast.setBackground(colors[((int) RCSolveMain.rubiksCube.getBack().getSouthEast() - 65)]);
    }
}