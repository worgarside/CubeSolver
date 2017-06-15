import java.util.ArrayList;
public class Solver{
    private static final int[] EDGE_MIDDLES = {1, 3, 5, 7, 10, 13, 16, 19, 21, 23, 24, 26, 27, 29, 30, 32, 34, 37, 40, 43, 46, 48, 50, 52};
    private static final int[] CORNERS = {0, 2, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 51, 53};
    private static final int[] ORDERED_CORNERS =  {0, 2, 6, 8, 35, 38, 41, 44, 33, 36, 39, 42, 45, 47, 51, 53, 11, 14, 17, 20, 9, 12, 15, 18};

    public static void whiteToTop(Cube cube){
        if(cube.getTop().getCentre() != 'W'){
           if(cube.getBottom().getCentre() == 'W'){
               cube.moveX2();
           }

           if(cube.getRight().getCentre() == 'W'){
               cube.moveNotZ();
           }

           if(cube.getLeft().getCentre() == 'W'){
               cube.moveZ();
           }

           if(cube.getFront().getCentre() == 'W'){
               cube.moveX();
           }

           if(cube.getBack().getCentre() == 'W'){
               cube.moveNotX();
           }
        }
    }

    public static ArrayList<Integer> updateWhiteMiddles(String cubeWord){
        ArrayList<Integer> tempWhiteMiddles = new ArrayList<Integer>();
        for(int i = 0; i < EDGE_MIDDLES.length; i++){
            if (cubeWord.charAt(EDGE_MIDDLES[i]) == 'W'){
                tempWhiteMiddles.add(EDGE_MIDDLES[i]);
            }
        }
        return tempWhiteMiddles;
    }

    public static void whiteCrossYellowCentre(Cube cube){
        ArrayList<Integer> whiteMiddles = new ArrayList<Integer>();
        whiteMiddles = updateWhiteMiddles(cube.toWord());
        System.out.println(whiteMiddles);
        while(!(whiteMiddles.get(0) == 46 || whiteMiddles.get(0) == 48 || whiteMiddles.get(0) == 50 || whiteMiddles.get(0) == 52 )){
            switch (whiteMiddles.get(0)) {
                case 1:
                    if (!whiteMiddles.contains(52)) {
                        cube.moveB2();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveD();
                        cube.moveB2();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveNotD();
                        cube.moveB2();
                    } else {
                        cube.moveD2();
                        cube.moveB2();
                    }
                    break;
                case 3:
                    if (!whiteMiddles.contains(48)) {
                        cube.moveL();
                        cube.moveL();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveD();
                        cube.moveL2();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveNotD();
                        cube.moveL2();
                    } else {
                        cube.moveD2();
                        cube.moveL2();
                    }
                    break;
                case 5:
                    if (!whiteMiddles.contains(50)) {
                        cube.moveR2();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveD();
                        cube.moveR2();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveNotD();
                        cube.moveR2();
                    } else {
                        cube.moveD2();
                        cube.moveR2();
                    }
                    break;
                case 7:
                    if (!whiteMiddles.contains(46)) {
                        cube.moveF2();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveD();
                        cube.moveF2();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveNotD();
                        cube.moveF2();
                    } else {
                        cube.moveD2();
                        cube.moveF2();
                    }
                    break;
                case 10:
                    if (!whiteMiddles.contains(48)) {
                        cube.moveL();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveD();
                        cube.moveL();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveNotD();
                        cube.moveL();
                    } else {
                        cube.moveD2();
                        cube.moveL();
                    }
                    break;
                case 13:
                    if (!whiteMiddles.contains(46)) {
                        cube.moveF();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveD();
                        cube.moveF();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveNotD();
                        cube.moveF();
                    } else {
                        cube.moveD2();
                        cube.moveF();
                    }
                    break;
                case 16:
                    if (!whiteMiddles.contains(50)) {
                        cube.moveNotR();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveD();
                        cube.moveNotR();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveNotD();
                        cube.moveNotR();
                    } else {
                        cube.moveD2();
                        cube.moveNotR();
                    }
                    break;
                case 19:
                    if (!whiteMiddles.contains(52)) {
                        cube.moveB();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveD();
                        cube.moveB();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveNotD();
                        cube.moveB();
                    } else {
                        cube.moveD2();
                        cube.moveB();
                    }
                    break;
                case 21:
                    if (!whiteMiddles.contains(52)) {
                        cube.moveB();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveD();
                        cube.moveB();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveNotD();
                        cube.moveB();
                    } else {
                        cube.moveD2();
                        cube.moveB();
                    }
                    break;
                case 23:
                    if (!whiteMiddles.contains(46)) {
                        cube.moveNotF();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveD();
                        cube.moveNotF();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveNotD();
                        cube.moveNotF();
                    } else {
                        cube.moveD2();
                        cube.moveNotF();
                    }
                    break;
                case 24:
                    if (!whiteMiddles.contains(48)) {
                        cube.moveL();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveD();
                        cube.moveL();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveNotD();
                        cube.moveL();
                    } else {
                        cube.moveD2();
                        cube.moveL();
                    }
                    break;
                case 26:
                    if (!whiteMiddles.contains(50)) {
                        cube.moveNotR();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveD();
                        cube.moveNotR();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveNotD();
                        cube.moveNotR();
                    } else {
                        cube.moveD2();
                        cube.moveNotR();
                    }
                    break;
                case 27:
                    if (!whiteMiddles.contains(46)) {
                        cube.moveF();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveD();
                        cube.moveF();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveNotD();
                        cube.moveF();
                    } else {
                        cube.moveD2();
                        cube.moveF();
                    }
                    break;
                case 29:
                    if (!whiteMiddles.contains(52)) {
                        cube.moveNotB();
                    } else if (!whiteMiddles.contains(50)) {
                        cube.moveD();
                        cube.moveNotB();
                    } else if (!whiteMiddles.contains(48)) {
                        cube.moveNotD();
                        cube.moveNotB();
                    } else {
                        cube.moveD2();
                        cube.moveNotB();
                    }
                    break;
                case 30:
                    if (!whiteMiddles.contains(50)) {
                        cube.moveR();
                    } else if (!whiteMiddles.contains(46)) {
                        cube.moveD();
                        cube.moveR();
                    } else if (!whiteMiddles.contains(52)) {
                        cube.moveNotD();
                        cube.moveR();
                    } else {
                        cube.moveD2();
                        cube.moveR();
                    }
                    break;
                case 32:
                    if (!whiteMiddles.contains(48)) {
                        cube.moveNotL();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveD();
                        cube.moveNotL();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveNotD();
                        cube.moveNotL();
                    } else {
                        cube.moveD2();
                        cube.moveNotL();
                    }
                    break;
                case 34:
                    if (!whiteMiddles.contains(48)) {
                        cube.moveNotL();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveD();
                        cube.moveNotL();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveNotD();
                        cube.moveNotL();
                    } else {
                        cube.moveD2();
                        cube.moveNotL();
                    }
                    break;
                case 37:
                    if (!whiteMiddles.contains(46)) {
                        cube.moveNotF();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveD();
                        cube.moveNotF();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveNotD();
                        cube.moveNotF();
                    } else {
                        cube.moveD2();
                        cube.moveNotF();
                    }
                    break;
                case 40:
                    if (!whiteMiddles.contains(50)) {
                        cube.moveNotR();
                    } else if (!(whiteMiddles.contains(46))) {
                        cube.moveD();
                        cube.moveNotR();
                    } else if (!(whiteMiddles.contains(52))) {
                        cube.moveNotD();
                        cube.moveNotR();
                    } else {
                        cube.moveD2();
                        cube.moveNotR();
                    }
                    break;
                case 43:
                    if (!whiteMiddles.contains(52)) {
                        cube.moveNotB();
                    } else if (!(whiteMiddles.contains(50))) {
                        cube.moveD();
                        cube.moveNotB();
                    } else if (!(whiteMiddles.contains(48))) {
                        cube.moveNotD();
                        cube.moveNotB();
                    } else {
                        cube.moveD2();
                        cube.moveNotB();
                    }
                    break;
            }
            whiteMiddles = updateWhiteMiddles(cube.toWord());
            System.out.println();
            System.out.print(whiteMiddles);
        }
    }

    public static void whiteCross(Cube cube){
        while(!(cube.getFront().getCentre() == cube.getFront().getSouth() && cube.getBottom().getNorth() == 'W')){
            cube.moveD();
        }
        cube.moveF2();

        while(!(cube.getLeft().getCentre() == cube.getLeft().getSouth() && cube.getBottom().getWest() == 'W')){
            cube.moveD();
        }
        cube.moveL2();

        while(!(cube.getRight().getCentre() == cube.getRight().getSouth() && cube.getBottom().getEast() == 'W')){
            cube.moveD();
        }
        cube.moveR2();

        while(!(cube.getBack().getCentre() == cube.getBack().getSouth() && cube.getBottom().getSouth() == 'W')){
            cube.moveD();
        }
        cube.moveB2();
    }

    public static ArrayList<Integer> updateWhiteCorners(String cubeWord){
        ArrayList<Integer> tempWhiteCorners = new ArrayList<Integer>();
        for(int i = 0; i < ORDERED_CORNERS.length; i++){
            if (cubeWord.charAt(ORDERED_CORNERS[i]) == 'W'){
                tempWhiteCorners.add(ORDERED_CORNERS[i]);
            }
        }
        return tempWhiteCorners;
    }

    public static void completeWhiteFace(Cube cube){
        ArrayList<Integer> whiteCorners = new ArrayList<Integer>();
        whiteCorners = updateWhiteCorners(cube.toWord());
        System.out.println(whiteCorners);
        for (int i = 0; i < whiteCorners.size(); i++) {
            String cubeWord = cube.toWord();
            switch (whiteCorners.get(i)) {
                case 0:
                    if(!(cubeWord.charAt(9) == cubeWord.charAt(10) && cubeWord.charAt(20) == cubeWord.charAt(19))){
                        cube.moveNotL();
                        cube.moveNotD();
                        cube.moveL();
                    }
                    break;
                case 2:
                    if(!(cubeWord.charAt(17) == cubeWord.charAt(16) && cubeWord.charAt(18) == cubeWord.charAt(19))){
                        cube.moveR();
                        cube.moveD();
                        cube.moveNotR();
                    }
                    break;
                case 6:
                    if(!(cubeWord.charAt(11) == cubeWord.charAt(10) && cubeWord.charAt(12) == cubeWord.charAt(13))){
                        cube.moveL();
                        cube.moveD();
                        cube.moveNotL();
                    }
                    break;
                case 8:
                    if(!(cubeWord.charAt(14) == cubeWord.charAt(13) && cubeWord.charAt(15) == cubeWord.charAt(16))){
                        cube.moveNotR();
                        cube.moveNotD();
                        cube.moveR();
                    }
                    break;
                case 9:
                    cube.moveB();
                    cube.moveNotD();
                    cube.moveNotB();
                    break;
                case 11:
                    cube.moveNotF();
                    cube.moveD();
                    cube.moveF();
                    break;
                case 12:
                    cube.moveL();
                    cube.moveNotD();
                    cube.moveNotL();
                    break;
                case 14:
                    cube.moveNotR();
                    cube.moveD();
                    cube.moveR();
                    break;
                case 15:
                    cube.moveF();
                    cube.moveNotD();
                    cube.moveNotF();
                    break;
                case 17:
                    cube.moveNotB();
                    cube.moveD();
                    cube.moveB();
                    break;
                case 18:
                    cube.moveR();
                    cube.moveNotD();
                    cube.moveNotR();
                    break;
                case 20:
                    cube.moveNotL();
                    cube.moveD();
                    cube.moveL();
                    break;
                case 33:
                    while(cubeWord.charAt(44) != cubeWord.charAt(31)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveD();
                    cube.moveB();
                    cube.moveNotD();
                    cube.moveNotB();
                    break;
                case 35:
                    while(cubeWord.charAt(36) != cubeWord.charAt(25)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveNotD();
                    cube.moveNotF();
                    cube.moveD();
                    cube.moveF();
                    break;
                case 36:
                    while(cubeWord.charAt(35) != cubeWord.charAt(22)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveD();
                    cube.moveL();
                    cube.moveNotD();
                    cube.moveNotL();
                    break;
                case 38:
                    while(cubeWord.charAt(39) != cubeWord.charAt(28)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveNotD();
                    cube.moveNotR();
                    cube.moveD();
                    cube.moveR();
                    break;
                case 39:
                    while(cubeWord.charAt(38) != cubeWord.charAt(25)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveD();
                    cube.moveF();
                    cube.moveNotD();
                    cube.moveNotF();
                    break;
                case 41:
                    while(cubeWord.charAt(42) != cubeWord.charAt(31)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveNotD();
                    cube.moveNotB();
                    cube.moveD();
                    cube.moveB();
                    break;
                case 42:
                    while(cubeWord.charAt(41) != cubeWord.charAt(28)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveD();
                    cube.moveR();
                    cube.moveNotD();
                    cube.moveNotR();
                    break;
                case 44:
                    while(cubeWord.charAt(33) != cubeWord.charAt(22)) {
                        cube.moveU();
                        cube.moveNotE();
                    }
                    cube.moveNotD();
                    cube.moveNotL();
                    cube.moveD();
                    cube.moveL();
                    break;
                case 45:
                    cube.moveL();
                    cube.moveNotD();
                    cube.moveNotL();
                    break;
                case 47:
                    cube.moveNotR();
                    cube.moveD();
                    cube.moveR();
                    break;
                case 51:
                    cube.moveNotL();
                    cube.moveD();
                    cube.moveL();
                    break;
                case 53:
                    cube.moveR();
                    cube.moveNotD();
                    cube.moveNotR();
                    break;
            }

        }

    }
}