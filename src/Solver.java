import java.util.ArrayList;
public class Solver{
    private static final int[] EDGE_MIDDLES = {1, 3, 5, 7, 10, 13, 16, 19, 21, 23, 24, 26, 27, 29, 30, 32, 34, 37, 40, 43, 46, 48, 50, 52};
    private static final int[] CORNERS = {0, 2, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 51, 53};
    private static final int[] ORDERED_CORNERS =  {0, 2, 6, 8, 35, 38, 41, 44, 33, 36, 39, 42, 45, 47, 51, 53, 11, 14, 17, 20, 9, 12, 15, 18};
    private static final int[][] TOP_ROW_MIDDLES = {{10, 3}, {13, 7}, {16, 5}, {19, 1}};
    private static final int[][] MIDDLE_ROW= {{21, 22}, {22, 23}, {24, 25}, {25, 26}, {27, 28}, {28, 29}, {30, 31}, {31, 32}};

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
        int currentCorner = 0;

        while(!(whiteCorners.contains(0) && whiteCorners.contains(2) && whiteCorners.contains(6) && whiteCorners.contains(8))){
            String cubeWord = cube.toWord();
            switch (whiteCorners.get(currentCorner)) {
                case 0:
                    if(!(cubeWord.charAt(9) == cubeWord.charAt(10) && cubeWord.charAt(20) == cubeWord.charAt(19))){
                        cube.moveNotL();
                        cube.moveNotD();
                        cube.moveL();
                    }else{
                        currentCorner ++;
                    }
                    break;
                case 2:
                    if(!(cubeWord.charAt(17) == cubeWord.charAt(16) && cubeWord.charAt(18) == cubeWord.charAt(19))){
                        cube.moveR();
                        cube.moveD();
                        cube.moveNotR();
                    }else{
                        currentCorner ++;
                    }
                    break;
                case 6:
                    if(!(cubeWord.charAt(11) == cubeWord.charAt(10) && cubeWord.charAt(12) == cubeWord.charAt(13))){
                        cube.moveL();
                        cube.moveD();
                        cube.moveNotL();

                    }else{
                        currentCorner ++;
                    }
                    break;
                case 8:
                    if(!(cubeWord.charAt(14) == cubeWord.charAt(13) && cubeWord.charAt(15) == cubeWord.charAt(16))){
                        cube.moveNotR();
                        cube.moveNotD();
                        cube.moveR();
                    }else{
                        currentCorner ++;
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
                        cubeWord = cube.toWord();
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
            whiteCorners = updateWhiteCorners(cube.toWord());
        }
        cube.moveZ2();
    }

    public static void secondRow(Cube cube){
        String cubeWord = cube.toWord();

        if((cubeWord.charAt(1) == 'Y' || cubeWord.charAt(19) == 'Y') && (cubeWord.charAt(3) == 'Y' || cubeWord.charAt(10) == 'Y')
                && (cubeWord.charAt(5) == 'Y' || cubeWord.charAt(16) == 'Y') && (cubeWord.charAt(7) == 'Y' || cubeWord.charAt(13) == 'Y')){ //If all cubies on top are invalid (have yellow)

            cube.moveU();
            cube.moveR();
            cube.moveNotU();
            cube.moveNotR();
            cube.moveF();
            cube.moveNotR();
            cube.moveNotF();
            cube.moveR();

            cubeWord = cube.toWord();
        }

        int invalidCubieCount = 0;
        while(!((cubeWord.charAt(21) == cubeWord.charAt(22) && cubeWord.charAt(22) == cubeWord.charAt(23)) &&
                (cubeWord.charAt(24) == cubeWord.charAt(25) && cubeWord.charAt(25) == cubeWord.charAt(26)) &&
                (cubeWord.charAt(27) == cubeWord.charAt(28) && cubeWord.charAt(28) == cubeWord.charAt(29)) &&
                (cubeWord.charAt(30) == cubeWord.charAt(31) && cubeWord.charAt(31) == cubeWord.charAt(32)))){

            invalidCubieCount++;
            if(invalidCubieCount > 4){ //If there are more than 4 invalid cubies on the top face (impossible!), then the corner middles are correct, but inverted

                for(int i = 0; i < MIDDLE_ROW.length; i++){ //For each middle cubie...
                    if(!(cubeWord.charAt(MIDDLE_ROW[i][0]) == cubeWord.charAt(MIDDLE_ROW[i][1]))){ //...if it's inverted...
                        switch(MIDDLE_ROW[i][0]){ //...fix it!
                            case 21:
                                cube.moveNotU();
                                cube.moveNotB();
                                cube.moveU();
                                cube.moveB();
                                cube.moveNotL();
                                cube.moveB();
                                cube.moveL();
                                cube.moveNotB();
                                break;
                            case 22:
                                cube.moveU();
                                cube.moveF();
                                cube.moveNotU();
                                cube.moveNotF();
                                cube.moveL();
                                cube.moveNotF();
                                cube.moveNotL();
                                cube.moveF();
                                break;
                            case 24:
                                cube.moveNotU();
                                cube.moveNotL();
                                cube.moveU();
                                cube.moveL();
                                cube.moveNotF();
                                cube.moveL();
                                cube.moveF();
                                cube.moveNotL();
                                break;
                            case 25:
                                cube.moveU();
                                cube.moveR();
                                cube.moveNotU();
                                cube.moveNotR();
                                cube.moveF();
                                cube.moveNotR();
                                cube.moveNotF();
                                cube.moveR();
                                break;
                            case 27:
                                cube.moveNotU();
                                cube.moveNotF();
                                cube.moveU();
                                cube.moveF();
                                cube.moveNotR();
                                cube.moveF();
                                cube.moveR();
                                cube.moveNotF();
                                break;
                            case 28:
                                cube.moveU();
                                cube.moveB();
                                cube.moveNotU();
                                cube.moveNotB();
                                cube.moveR();
                                cube.moveNotB();
                                cube.moveNotR();
                                cube.moveB();
                                break;
                            case 30:
                                cube.moveNotU();
                                cube.moveNotR();
                                cube.moveU();
                                cube.moveR();
                                cube.moveNotB();
                                cube.moveR();
                                cube.moveB();
                                cube.moveNotR();
                                break;
                            case 31:
                                cube.moveU();
                                cube.moveL();
                                cube.moveNotU();
                                cube.moveNotL();
                                cube.moveB();
                                cube.moveNotL();
                                cube.moveNotB();
                                cube.moveL();
                                break;
                            default:
                                System.out.println("ERROR #4");
                                System.exit(1);
                        }
                    }
                }
            }

            for(int i = 0; i < TOP_ROW_MIDDLES.length; i++) {//For each top cubie...


                cubeWord = cube.toWord();

                if(cubeWord.charAt(TOP_ROW_MIDDLES[i][0]) != 'Y' && cubeWord.charAt(TOP_ROW_MIDDLES[i][1]) != 'Y' ){ //...if it is a valid cubie (i.e. not part yellow)


                    int correctionCount = 0;
                    while(!(cubeWord.charAt(TOP_ROW_MIDDLES[i][0]) == cubeWord.charAt(TOP_ROW_MIDDLES[i][0] + 12))){//If current cubie is not on correct face
                        cube.moveD();
                        cube.moveE();

                        cubeWord = cube.toWord();
                        correctionCount ++;
                        if(correctionCount > 4){
                            System.exit(1);
                        }
                    }


                    int relLeftCentre = TOP_ROW_MIDDLES[i][0]+9;
                    if(relLeftCentre < 21){ relLeftCentre += 12; }

                    int relRightCentre = TOP_ROW_MIDDLES[i][0]+15;
                    if(relRightCentre > 32){ relRightCentre -= 12; }

                    if(cubeWord.charAt(relLeftCentre) == cubeWord.charAt(TOP_ROW_MIDDLES[i][1])){ //If top matches relLeft face...
                        switch(TOP_ROW_MIDDLES[i][0]){ //... then depending on which face we're currently on, moveTopToLeft...
                            case 10:
                                cube.moveNotU();
                                cube.moveNotB();
                                cube.moveU();
                                cube.moveB();
                                cube.moveNotL();
                                cube.moveB();
                                cube.moveL();
                                cube.moveNotB();
                                break;
                            case 13:
                                cube.moveNotU();
                                cube.moveNotL();
                                cube.moveU();
                                cube.moveL();
                                cube.moveNotF();
                                cube.moveL();
                                cube.moveF();
                                cube.moveNotL();
                                break;
                            case 16:
                                cube.moveNotU();
                                cube.moveNotF();
                                cube.moveU();
                                cube.moveF();
                                cube.moveNotR();
                                cube.moveF();
                                cube.moveR();
                                cube.moveNotF();
                                break;
                            case 19:
                                cube.moveNotU();
                                cube.moveNotR();
                                cube.moveU();
                                cube.moveR();
                                cube.moveNotB();
                                cube.moveR();
                                cube.moveB();
                                cube.moveNotR();
                                break;
                            default:
                                System.out.println("ERROR #1");
                                System.exit(1);
                        }
                        cubeWord = cube.toWord();

                    }else if(cubeWord.charAt(relRightCentre) == cubeWord.charAt(TOP_ROW_MIDDLES[i][1])){
                        switch(TOP_ROW_MIDDLES[i][0]){ //...or moveTopToRight
                            case 10:
                                cube.moveU();
                                cube.moveF();
                                cube.moveNotU();
                                cube.moveNotF();
                                cube.moveL();
                                cube.moveNotF();
                                cube.moveNotL();
                                cube.moveF();
                                break;
                            case 13:
                                cube.moveU();
                                cube.moveR();
                                cube.moveNotU();
                                cube.moveNotR();
                                cube.moveF();
                                cube.moveNotR();
                                cube.moveNotF();
                                cube.moveR();
                                break;
                            case 16:
                                cube.moveU();
                                cube.moveB();
                                cube.moveNotU();
                                cube.moveNotB();
                                cube.moveR();
                                cube.moveNotB();
                                cube.moveNotR();
                                cube.moveB();
                                break;
                            case 19:
                                cube.moveU();
                                cube.moveL();
                                cube.moveNotU();
                                cube.moveNotL();
                                cube.moveB();
                                cube.moveNotL();
                                cube.moveNotB();
                                cube.moveL();
                                break;
                            default:
                                System.out.println("ERROR #2");
                                System.exit(1);
                        }
                        cubeWord = cube.toWord();
                    }
                }
            }
        }
    }

    public static void yellowFace(Cube cube){
        System.out.println("\nyellowFace");
        String cubeWord = cube.toWord();

        /*
        String cubeWordTop = "";
        for(int i = 0; i < 9; i++){
            if(cubeWord.charAt(i) == 'Y'){
                cubeWordTop += '1';
            }else{
                cubeWordTop += '0';
            }
            cubeWordTop += cubeWord.charAt(i);
        }

        switch(cubeWordTop){
            case ""
        }
        */
        while(!(cubeWord.charAt(0) == 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) == 'Y' &&
                cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                cubeWord.charAt(6) == 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) == 'Y')){

            if(cubeWord.charAt(1) != 'Y' && cubeWord.charAt(3) != 'Y' && cubeWord.charAt(5) != 'Y' && cubeWord.charAt(7) != 'Y'){
                System.out.println("single yellow");
                cube.moveF();
                cube.moveR();
                cube.moveU();
                cube.moveNotR();
                cube.moveNotU();
                cube.moveNotF();
                cubeWord = cube.toWord();
            }

            if((cubeWord.charAt(1) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(7) == 'Y') && (cubeWord.charAt(3) != 'Y' || cubeWord.charAt(5) != 'Y')){ //Vertical bar
                System.out.println("vertical bar");
                cube.moveR();
                cube.moveB();
                cube.moveU();
                cube.moveNotB();
                cube.moveNotU();
                cube.moveNotR();
                cubeWord = cube.toWord();
            }

            if((cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y') && (cubeWord.charAt(1) != 'Y' || cubeWord.charAt(7) != 'Y')){
                System.out.println("horizontal bar");
                cube.moveF();
                cube.moveR();
                cube.moveU();
                cube.moveNotR();
                cube.moveNotU();
                cube.moveNotF();
                cubeWord = cube.toWord();
            }

            if((cubeWord.charAt(1) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y') && (cubeWord.charAt(3) != 'Y' && cubeWord.charAt(7) != 'Y')){
                System.out.println("top right hook");
                cube.moveL();
                cube.moveU();
                cube.moveF();
                cube.moveNotU();
                cube.moveNotF();
                cube.moveNotL();
                cubeWord = cube.toWord();
            }

            if((cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' && cubeWord.charAt(7) == 'Y') && (cubeWord.charAt(1) != 'Y' && cubeWord.charAt(3) != 'Y')){
                System.out.println("bottom right hook");
                cube.moveB();
                cube.moveU();
                cube.moveL();
                cube.moveNotU();
                cube.moveNotL();
                cube.moveNotB();
                cubeWord = cube.toWord();
            }

            if((cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(7) == 'Y') && (cubeWord.charAt(1) != 'Y' && cubeWord.charAt(5) != 'Y')){
                System.out.println("bottom left hook");
                cube.moveR();
                cube.moveU();
                cube.moveB();
                cube.moveNotU();
                cube.moveNotB();
                cube.moveNotR();
                cubeWord = cube.toWord();
            }

            if((cubeWord.charAt(1) == 'Y' && cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y') && (cubeWord.charAt(5) != 'Y' && cubeWord.charAt(7) != 'Y')){
                System.out.println("top left hook");
                cube.moveF();
                cube.moveU();
                cube.moveR();
                cube.moveNotU();
                cube.moveNotR();
                cube.moveNotF();
                cubeWord = cube.toWord();
            }

            if(!(cubeWord.charAt(1) == 'Y' && cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' && cubeWord.charAt(7) == 'Y')){
                System.out.println("ERROR #3");
                System.exit(1);
            }

            if(cubeWord.charAt(0) == 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) == 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.println("right sign");
                cube.moveB();
                cube.moveU();
                cube.moveNotB();
                cube.moveU();
                cube.moveB();
                cube.moveU2();
                cube.moveNotB();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) == 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) == 'Y'){
                System.out.println("top sign");
                cube.moveL();
                cube.moveU();
                cube.moveNotL();
                cube.moveU();
                cube.moveL();
                cube.moveU2();
                cube.moveNotL();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) == 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) == 'Y'){
                System.out.println("left sign");
                cube.moveF();
                cube.moveU();
                cube.moveNotF();
                cube.moveU();
                cube.moveF();
                cube.moveU2();
                cube.moveNotF();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) == 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) == 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.println("down sign");
                cube.moveR();
                cube.moveU();
                cube.moveNotR();
                cube.moveU();
                cube.moveR();
                cube.moveU2();
                cube.moveNotR();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.println("cross");

                if(cubeWord.charAt(18) == 'Y' && cubeWord.charAt(20) == 'Y'){
                    cube.moveR();
                    cube.moveU();
                    cube.moveNotR();
                    cube.moveU();
                    cube.moveR();
                    cube.moveU2();
                    cube.moveNotR();
                    cubeWord = cube.toWord();
                }else if(cubeWord.charAt(15) == 'Y' && cubeWord.charAt(17) == 'Y'){
                    cube.moveF();
                    cube.moveU();
                    cube.moveNotF();
                    cube.moveU();
                    cube.moveF();
                    cube.moveU2();
                    cube.moveNotF();
                    cubeWord = cube.toWord();
                }else if(cubeWord.charAt(12) == 'Y' && cubeWord.charAt(14) == 'Y'){
                    cube.moveL();
                    cube.moveU();
                    cube.moveNotL();
                    cube.moveU();
                    cube.moveL();
                    cube.moveU2();
                    cube.moveNotL();
                    cubeWord = cube.toWord();
                }else if(cubeWord.charAt(9) == 'Y' && cubeWord.charAt(11) == 'Y'){
                    cube.moveB();
                    cube.moveU();
                    cube.moveNotB();
                    cube.moveU();
                    cube.moveB();
                    cube.moveU2();
                    cube.moveNotB();
                    cubeWord = cube.toWord();
                }else{
                    cube.moveR();
                    cube.moveU();
                    cube.moveNotR();
                    cube.moveU();
                    cube.moveR();
                    cube.moveU2();
                    cube.moveNotR();
                    cubeWord = cube.toWord();
                }
            }



            if(cubeWord.charAt(0) == 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.print("top left fish");
                cube.moveF();
                cube.moveU();
                cube.moveNotF();
                cube.moveU();
                cube.moveF();
                cube.moveU2();
                cube.moveNotF();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) == 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.print("top right fish");
                cube.moveL();
                cube.moveU();
                cube.moveNotL();
                cube.moveU();
                cube.moveL();
                cube.moveU2();
                cube.moveNotL();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) == 'Y'){
                System.out.print("bottom right fish");
                cube.moveB();
                cube.moveU();
                cube.moveNotB();
                cube.moveU();
                cube.moveB();
                cube.moveU2();
                cube.moveNotB();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) == 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.print("bottom left fish");
                cube.moveR();
                cube.moveU();
                cube.moveNotR();
                cube.moveU();
                cube.moveR();
                cube.moveU2();
                cube.moveNotR();
                cubeWord = cube.toWord();
            }

            if(cubeWord.charAt(0) != 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) == 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) == 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) != 'Y'){
                System.out.print("BL-TR diag squares");
                cube.moveR();
                cube.moveU();
                cube.moveNotR();
                cube.moveU();
                cube.moveR();
                cube.moveU2();
                cube.moveNotR();
                cubeWord = cube.toWord();

            }

            if(cubeWord.charAt(0) == 'Y' && cubeWord.charAt(1) == 'Y' && cubeWord.charAt(2) != 'Y' &&
                    cubeWord.charAt(3) == 'Y' && cubeWord.charAt(4) == 'Y' && cubeWord.charAt(5) == 'Y' &&
                    cubeWord.charAt(6) != 'Y' && cubeWord.charAt(7) == 'Y' && cubeWord.charAt(8) == 'Y'){
                System.out.print("TL-BR diag squares");

                cube.moveR();
                cube.moveU();
                cube.moveNotR();
                cube.moveU();
                cube.moveR();
                cube.moveU2();
                cube.moveNotR();
                cubeWord = cube.toWord();
//                yellowFace(cube);
            }
            System.out.println("Yellow complete?");
        }

    }
}