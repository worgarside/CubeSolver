import java.util.ArrayList;
public class Solver{
    private static final int[] EDGE_MIDDLES = {1, 3, 5, 7, 10, 13, 16, 19, 21, 23, 24, 26, 27, 29, 30, 32, 34, 37, 40, 43, 46, 48, 50, 52};

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

        do{
            for (int i = 0; i < whiteMiddles.size(); i++) {
                switch (whiteMiddles.get(i)) {
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
            }
        }while(!(whiteMiddles.contains(46) && whiteMiddles.contains(48) && whiteMiddles.contains(50) && whiteMiddles.contains(52)));
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

    public static void completeWhiteFace(Cube cube){

    }
}