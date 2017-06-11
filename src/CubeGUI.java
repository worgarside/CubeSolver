import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.*;
import javax.swing.*;
import java.awt.Color;

@SuppressWarnings("serial")
public class CubeGUI extends JFrame {
    final int WIDTH = 1080;
    final int HEIGHT = 720;

    public CubeGUI() {
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

        JPanel topNorthWest = new JPanel();
        topNorthWest.setBackground(Color.WHITE);
        topNorthWest.setBounds(240, 120, 40, 40);
        topNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topNorthWest);

        JPanel topNorth = new JPanel();
        topNorth.setBackground(Color.WHITE);
        topNorth.setBounds(290, 120, 40, 40);
        topNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topNorth);

        JPanel topNorthEast = new JPanel();
        topNorthEast.setBackground(Color.WHITE);
        topNorthEast.setBounds(340, 120, 40, 40);
        topNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topNorthEast);

        JPanel topWest = new JPanel();
        topWest.setBackground(Color.WHITE);
        topWest.setBounds(240, 170, 40, 40);
        topWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topWest);

        JPanel topCentre = new JPanel();
        topCentre.setBackground(Color.WHITE);
        topCentre.setBounds(290, 170, 40, 40);
        topCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topCentre);

        JPanel topEast = new JPanel();
        topEast.setBackground(Color.WHITE);
        topEast.setBounds(340, 170, 40, 40);
        topEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topEast);

        JPanel topSouthWest = new JPanel();
        topSouthWest.setBackground(Color.WHITE);
        topSouthWest.setBounds(240, 220, 40, 40);
        topSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topSouthWest);

        JPanel topSouth = new JPanel();
        topSouth.setBackground(Color.WHITE);
        topSouth.setBounds(290, 220, 40, 40);
        topSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topSouth);

        JPanel topSouthEast = new JPanel();
        topSouthEast.setBackground(Color.WHITE);
        topSouthEast.setBounds(340, 220, 40, 40);
        topSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(topSouthEast);

        //******** BOTTOM SIDE ********\\

        JPanel bottomNorthWest = new JPanel();
        bottomNorthWest.setBackground(Color.YELLOW);
        bottomNorthWest.setBounds(240, 420, 40, 40);
        bottomNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomNorthWest);

        JPanel bottomNorth = new JPanel();
        bottomNorth.setBackground(Color.YELLOW);
        bottomNorth.setBounds(290, 420, 40, 40);
        bottomNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomNorth);

        JPanel bottomNorthEast = new JPanel();
        bottomNorthEast.setBackground(Color.YELLOW);
        bottomNorthEast.setBounds(340, 420, 40, 40);
        bottomNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomNorthEast);

        JPanel bottomWest = new JPanel();
        bottomWest.setBackground(Color.YELLOW);
        bottomWest.setBounds(240, 470, 40, 40);
        bottomWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomWest);

        JPanel bottomCentre = new JPanel();
        bottomCentre.setBackground(Color.YELLOW);
        bottomCentre.setBounds(290, 470, 40, 40);
        bottomCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomCentre);

        JPanel bottomEast = new JPanel();
        bottomEast.setBackground(Color.YELLOW);
        bottomEast.setBounds(340, 470, 40, 40);
        bottomEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomEast);

        JPanel bottomSouthWest = new JPanel();
        bottomSouthWest.setBackground(Color.YELLOW);
        bottomSouthWest.setBounds(240, 520, 40, 40);
        bottomSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomSouthWest);

        JPanel bottomSouth = new JPanel();
        bottomSouth.setBackground(Color.YELLOW);
        bottomSouth.setBounds(290, 520, 40, 40);
        bottomSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomSouth);

        JPanel bottomSouthEast = new JPanel();
        bottomSouthEast.setBackground(Color.YELLOW);
        bottomSouthEast.setBounds(340, 520, 40, 40);
        bottomSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(bottomSouthEast);

        //******** LEFT SIDE ********\\

        JPanel leftNorthWest = new JPanel();
        leftNorthWest.setBackground(new Color(255, 153, 0));
        leftNorthWest.setBounds(90, 270, 40, 40);
        leftNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftNorthWest);

        JPanel leftNorth = new JPanel();
        leftNorth.setBackground(new Color(255, 153, 0));
        leftNorth.setBounds(140, 270, 40, 40);
        leftNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftNorth);

        JPanel leftNorthEast = new JPanel();
        leftNorthEast.setBackground(new Color(255, 153, 0));
        leftNorthEast.setBounds(190, 270, 40, 40);
        leftNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftNorthEast);

        JPanel leftWest = new JPanel();
        leftWest.setBackground(new Color(255, 153, 0));
        leftWest.setBounds(90, 320, 40, 40);
        leftWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftWest);

        JPanel leftCentre = new JPanel();
        leftCentre.setBackground(new Color(255, 153, 0));
        leftCentre.setBounds(140, 320, 40, 40);
        leftCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftCentre);

        JPanel leftEast = new JPanel();
        leftEast.setBackground(new Color(255, 153, 0));
        leftEast.setBounds(190, 320, 40, 40);
        leftEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftEast);

        JPanel leftSouthWest = new JPanel();
        leftSouthWest.setBackground(new Color(255, 153, 0));
        leftSouthWest.setBounds(90, 370, 40, 40);
        leftSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftSouthWest);

        JPanel leftSouth = new JPanel();
        leftSouth.setBackground(new Color(255, 153, 0));
        leftSouth.setBounds(140, 370, 40, 40);
        leftSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftSouth);

        JPanel leftSouthEast = new JPanel();
        leftSouthEast.setBackground(new Color(255, 153, 0));
        leftSouthEast.setBounds(190, 370, 40, 40);
        leftSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(leftSouthEast);

        //******** RIGHT SIDE ********\\

        JPanel rightNorthWest = new JPanel();
        rightNorthWest.setBackground(Color.RED);
        rightNorthWest.setBounds(390, 270, 40, 40);
        rightNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightNorthWest);

        JPanel rightNorth = new JPanel();
        rightNorth.setBackground(Color.RED);
        rightNorth.setBounds(440, 270, 40, 40);
        rightNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightNorth);

        JPanel rightNorthEast = new JPanel();
        rightNorthEast.setBackground(Color.RED);
        rightNorthEast.setBounds(490, 270, 40, 40);
        rightNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightNorthEast);

        JPanel rightWest = new JPanel();
        rightWest.setBackground(Color.RED);
        rightWest.setBounds(390, 320, 40, 40);
        rightWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightWest);

        JPanel rightCentre = new JPanel();
        rightCentre.setBackground(Color.RED);
        rightCentre.setBounds(440, 320, 40, 40);
        rightCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightCentre);

        JPanel rightEast = new JPanel();
        rightEast.setBackground(Color.RED);
        rightEast.setBounds(490, 320, 40, 40);
        rightEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightEast);

        JPanel rightSouthWest = new JPanel();
        rightSouthWest.setBackground(Color.RED);
        rightSouthWest.setBounds(390, 370, 40, 40);
        rightSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightSouthWest);

        JPanel rightSouth = new JPanel();
        rightSouth.setBackground(Color.RED);
        rightSouth.setBounds(440, 370, 40, 40);
        rightSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightSouth);

        JPanel rightSouthEast = new JPanel();
        rightSouthEast.setBackground(Color.RED);
        rightSouthEast.setBounds(490, 370, 40, 40);
        rightSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(rightSouthEast);

        //******** FRONT SIDE ********\\

        JPanel frontNorthWest = new JPanel();
        frontNorthWest.setBackground(Color.GREEN);
        frontNorthWest.setBounds(240, 270, 40, 40);
        frontNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontNorthWest);

        JPanel frontNorth = new JPanel();
        frontNorth.setBackground(Color.GREEN);
        frontNorth.setBounds(290, 270, 40, 40);
        frontNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontNorth);

        JPanel frontNorthEast = new JPanel();
        frontNorthEast.setBackground(Color.GREEN);
        frontNorthEast.setBounds(340, 270, 40, 40);
        frontNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontNorthEast);

        JPanel frontWest = new JPanel();
        frontWest.setBackground(Color.GREEN);
        frontWest.setBounds(240, 320, 40, 40);
        frontWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontWest);

        JPanel frontCentre = new JPanel();
        frontCentre.setBackground(Color.GREEN);
        frontCentre.setBounds(290, 320, 40, 40);
        frontCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontCentre);

        JPanel frontEast = new JPanel();
        frontEast.setBackground(Color.GREEN);
        frontEast.setBounds(340, 320, 40, 40);
        frontEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontEast);

        JPanel frontSouthWest = new JPanel();
        frontSouthWest.setBackground(Color.GREEN);
        frontSouthWest.setBounds(240, 370, 40, 40);
        frontSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontSouthWest);

        JPanel frontSouth = new JPanel();
        frontSouth.setBackground(Color.GREEN);
        frontSouth.setBounds(290, 370, 40, 40);
        frontSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontSouth);

        JPanel frontSouthEast = new JPanel();
        frontSouthEast.setBackground(Color.GREEN);
        frontSouthEast.setBounds(340, 370, 40, 40);
        frontSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(frontSouthEast);

        //******** BACK SIDE ********\\

        JPanel backNorthWest = new JPanel();
        backNorthWest.setBackground(Color.BLUE);
        backNorthWest.setBounds(540, 270, 40, 40);
        backNorthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backNorthWest);

        JPanel backNorth = new JPanel();
        backNorth.setBackground(Color.BLUE);
        backNorth.setBounds(590, 270, 40, 40);
        backNorth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backNorth);

        JPanel backNorthEast = new JPanel();
        backNorthEast.setBackground(Color.BLUE);
        backNorthEast.setBounds(640, 270, 40, 40);
        backNorthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backNorthEast);

        JPanel backWest = new JPanel();
        backWest.setBackground(Color.BLUE);
        backWest.setBounds(540, 320, 40, 40);
        backWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backWest);

        JPanel backCentre = new JPanel();
        backCentre.setBackground(Color.BLUE);
        backCentre.setBounds(590, 320, 40, 40);
        backCentre.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backCentre);

        JPanel backEast = new JPanel();
        backEast.setBackground(Color.BLUE);
        backEast.setBounds(640, 320, 40, 40);
        backEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backEast);

        JPanel backSouthWest = new JPanel();
        backSouthWest.setBackground(Color.BLUE);
        backSouthWest.setBounds(540, 370, 40, 40);
        backSouthWest.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backSouthWest);

        JPanel backSouth = new JPanel();
        backSouth.setBackground(Color.BLUE);
        backSouth.setBounds(590, 370, 40, 40);
        backSouth.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backSouth);

        JPanel backSouthEast = new JPanel();
        backSouthEast.setBackground(Color.BLUE);
        backSouthEast.setBounds(640, 370, 40, 40);
        backSouthEast.setBorder(BorderFactory.createLineBorder(Color.black));
        contentPane.add(backSouthEast);




        JButton btnSolve = new JButton("Solve");
        contentPane.add(cubeNetPanel);
        contentPane.add(btnSolve);

        btnSolve.setBounds(WIDTH-100, HEIGHT-70, 80, 30);

        setVisible(true);
    }
}