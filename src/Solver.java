public class Solver{
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
        System.out.println(cubeWord);
        switch("W"){
            case cubeWord.charAt(0):
                System.out.println("TNW");
            default:
                System.out.println("nope");
        }
    }


}