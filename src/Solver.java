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

    public static void whiteCrossYellowCentre(Cube cube){
        String cubeWord = cube.toWord();
        ArrayList<Integer> whiteMiddles = new ArrayList<Integer>();

        for(int i = 0; i < EDGE_MIDDLES.length; i++){
            if (cubeWord.charAt(EDGE_MIDDLES[i]) == 'W'){
                 whiteMiddles.add(EDGE_MIDDLES[i]);
            }
        }

        for(int i = 0; i < whiteMiddles.size(); i++){

            switch(whiteMiddles.get(i)){
                case 1:
                    if(!whiteMiddles.contains(52)){
                        cube.moveB2();
                    }else if(!(whiteMiddles.contains(50))){
                        cube.moveD();
                    }else if(!(whiteMiddles.contains(48))){
                        cube.moveNotD();
                    }else{
                        cube.moveD2();
                    }
                    break;
                case 3:
                    if(!whiteMiddles.contains(48)){
                        cube.moveL2();
                    }else if(!(whiteMiddles.contains(52))){
                        cube.moveD();
                    }else if(!(whiteMiddles.contains(46))){
                    cube.moveNotD();
                }else{
                    cube.moveD2();
                }
                    break;
                case 5: if(!whiteMiddles.contains(50)){
                    cube.moveR2();
                }else if(!(whiteMiddles.contains(46))){
                    cube.moveD();
                }else if(!(whiteMiddles.contains(52))){
                    cube.moveNotD();
                }else{
                    cube.moveD2();
                }
                    break;
                case 7: if(!whiteMiddles.contains(46)){
                    cube.moveF2();
                }else if(!(whiteMiddles.contains(48))){
                    cube.moveD();
                }else if((!(whiteMiddles.contains(50)))){
                    cube.moveNotD();
                }else{
                    cube.moveD2();
                }
                    break;
                case 10:
                    if(!whiteMiddles.contains(46)){
                        cube.moveL();
                    }
                    break;
                case 13:
                    if(!whiteMiddles.contains(50)){
                        cube.moveF();
                    }
                    break;
                case 16:
                    if(!whiteMiddles.contains(46)){
                        cube.moveNotR();
                    }
                    break;
                case 19:
                    if(!whiteMiddles.contains(48)){
                        cube.moveB();
                    }
                    break;
                case 21:
                    if(!whiteMiddles.contains(52)){
                        cube.moveB();
                    }
                    break;
                case 23:
                    if(!whiteMiddles.contains(46)){
                        cube.moveNotF();
                    }
                    break;
                case 24:
                    if(!whiteMiddles.contains(48)){
                        cube.moveL();
                    }
                    break;
                case 26:
                    if(!whiteMiddles.contains(50)){
                        cube.moveNotR();
                    }
                    break;
                case 27:
                    if(!whiteMiddles.contains(46)){
                        cube.moveF();
                    }
                    break;
                case 29:
                    if(!whiteMiddles.contains(52)){
                        cube.moveNotB();
                    }
                    break;
                case 30:
                    if(!whiteMiddles.contains(50)){
                        cube.moveR();
                    }
                    break;
                case 32:
                    if(!whiteMiddles.contains(48)){
                        cube.moveNotL();
                    }
                    break;
                case 34:
                    if(!whiteMiddles.contains(46)){
                        cube.moveNotL();
                    }
                    break;
                case 37:
                    if(!whiteMiddles.contains(48)){
                        cube.moveF();
                    }
                    break;
                case 40:
                    if(!whiteMiddles.contains(46)){
                        cube.moveR();
                    }
                    break;
                case 43:
                    if(!whiteMiddles.contains(50)){
                        cube.moveB();
                    }
                    break;
            }

            /*
            if((whiteMiddles.get(i) == 1) && !(whiteMiddles.contains(52))){
                cube.moveB2();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 3) && !(whiteMiddles.contains(48))){
                cube.moveL2();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 5) && !(whiteMiddles.contains(50))){
                cube.moveR2();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 7) && !(whiteMiddles.contains(46))){
                cube.moveF2();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 10) && !(whiteMiddles.contains(46))){
                cube.moveL();
                cube.moveNotF();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 13) && !(whiteMiddles.contains(50))){
                cube.moveF();
                cube.moveNotR();
            }else{

            }

            if((whiteMiddles.get(i) == 16) && !(whiteMiddles.contains(46))){
                cube.moveNotR();
                cube.moveF();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 19) && !(whiteMiddles.contains(48))){
                cube.moveB();
                cube.moveNotL();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 21) && !(whiteMiddles.contains(52))){
                cube.moveB();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 23) && !(whiteMiddles.contains(46))){
                cube.moveNotF();
            }else{
                cube.moveD();
            }
            if((whiteMiddles.get(i) == 24) && !(whiteMiddles.contains(48))){
                cube.moveL();
            }else{
                cube.moveD();
            }
            if((whiteMiddles.get(i) == 26) && !(whiteMiddles.contains(50))){
                cube.moveNotR();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 27) && !(whiteMiddles.contains(46))){
                cube.moveF();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 29) && !(whiteMiddles.contains(52))){
                cube.moveNotB();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 30) && !(whiteMiddles.contains(50))){
                cube.moveR();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 32) && !(whiteMiddles.contains(48))){
                cube.moveNotL();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 34) && !(whiteMiddles.contains(46))){
                cube.moveNotL();
                cube.moveF();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 37) && !(whiteMiddles.contains(48))){
                cube.moveF();
                cube.moveL();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 40) && !(whiteMiddles.contains(46))){
                cube.moveR();
                cube.moveF();
            }else{
                cube.moveD();
            }

            if((whiteMiddles.get(i) == 43) && !(whiteMiddles.contains(50))){
                cube.moveB();
                cube.moveR();
            }else{
                cube.moveD();
            }
            */
        }

//        46
//        48
//        50
//        52



    }


}