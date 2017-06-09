public class Cube{
    private Side top;
    private Side left;
    private Side right;
    private Side bottom;
    private Side front;
    private Side back;
    public Cube(Side t, Side bo, Side l, Side r, Side f, Side ba){
        top = t;
        bottom = bo;
        left = l;
        right = r;
        front = f;
        back = ba;
    }

    // Accessor Methods
    public Side getTop(){
        return top;
    }
    public Side getLeft(){
        return left;
    }
    public Side getRight(){
        return right;
    }
    public Side getBottom(){
        return bottom;
    }
    public Side getFront(){
        return front;
    }
    public Side getBack(){
        return back;
    }

    @Override
    public String toString() {
        String result = "         " + top.getNorthWest() + "  " + top.getNorth() + "  " + top.getNorthEast() + "\n"
                + "         " + top.getWest() + "  " + top.getCentre() + "  " + top.getEast() + "\n"
                + "         " + top.getSouthWest() + "  " + top.getSouth() + "  " + top.getSouthEast() + "\n"
                + left.getNorthWest() + "  " + left.getNorth() + "  " + left.getNorthEast() + "  " + front.getNorthWest() + "  " + front.getNorth() + "  " + front.getNorthEast() + "  " + right.getNorthWest() + "  " + right.getNorth() + "  " + right.getNorthEast() + "  " + back.getNorthWest() + "  " + back.getNorth() + "  " + back.getNorthEast() + "\n"
                + left.getWest() + "  " + left.getCentre() + "  " + left.getEast() + "  " + front.getWest() + "  " + front.getCentre() + "  " + front.getEast() + "  " + right.getWest() + "  " + right.getCentre() + "  " + right.getEast() + "  " + back.getWest() + "  " + back.getCentre() + "  " + back.getEast() + "\n"
                + left.getSouthWest() + "  " + left.getSouth() + "  " + left.getSouthEast() + "  " + front.getSouthWest() + "  " + front.getSouth() + "  " + front.getSouthEast() + "  " + right.getSouthWest() + "  " + right.getSouth() + "  " + right.getSouthEast() + "  " + back.getSouthWest() + "  " + back.getSouth() + "  " + back.getSouthEast() + "\n"
                + "         " + bottom.getNorthWest() + "  " + bottom.getNorth() + "  " + bottom.getNorthEast() + "\n"
                + "         " + bottom.getWest() + "  " + bottom.getCentre() + "  " + bottom.getEast() + "\n"
                + "         " + bottom.getSouthWest() + "  " + bottom.getSouth() + "  " + bottom.getSouthEast() + "\n";
        return result;
    }

    public void displaySide(Solver.Direction direction){
        switch (direction){
            case TOP:
                System.out.println(top);
                break;
            case BOTTOM:
                System.out.println(bottom);
                break;
            case LEFT:
                System.out.println(left);
                break;
            case RIGHT:
                System.out.println(right);
                break;
            case FRONT:
                System.out.println(front);
                break;
            case BACK:
                System.out.println(back);
                break;
        }
    }

    public Side getSide(Solver.Direction direction){
        switch (direction){
            case TOP:
                return top;
            case BOTTOM:
                return bottom;
            case LEFT:
                return left;
            case RIGHT:
                return right;
            case FRONT:
                return front;
            case BACK:
                return back;
            default:
                Side tempSide = new Side('-', '-', '-', '-', '-', '-', '-', '-', '-');
                return tempSide;
        }

    }

    public boolean validateCube(){
        boolean valid = checkColourQuantity();

        return valid;
    }
    public boolean checkColourQuantity(){
        int[] alphabet = new int[26];
        for (Solver.Direction dir : Solver.Direction.values()) {
            for(int i = 0; i < 3; i ++){
                for(int j = 0; j < 3; j ++){
                    int[] coordArray = {i, j};
                    char currentCell = Character.toUpperCase(getSide(dir).getCell(coordArray));
                    alphabet[currentCell-'A'] ++;
                }
            }
        }
        System.out.println();
        for(int i = 0; i < alphabet.length; i++){
            System.out.print(((char) (i+65)) + ": " + alphabet[i] + ", ");
        }
        System.out.println("\n");

        if((alphabet[1] == 9) && (alphabet[6] == 9) && (alphabet[14] == 9) && (alphabet[17] == 9) && (alphabet[22] == 9) && (alphabet[24] == 9)){
            return true;
        }else{
            return false;
        }
    }

    public void moveR(){
        Cube tempCube = this;
        Cube newCube = this;

        top.setNorthEast(tempCube.getFront().getNorthEast());
        top.setEast(tempCube.getFront().getEast());
        top.setSouthEast(tempCube.getFront().getSouthEast());

        front.setNorthEast(tempCube.getBottom().getNorthEast());
        front.setEast(tempCube.getBottom().getEast());
        front.setSouthEast(tempCube.getBottom().getSouthEast());

        bottom.setNorthEast(tempCube.getBack().getNorthEast());
        bottom.setEast(tempCube.getBack().getEast());
        bottom.setSouthEast(tempCube.getBack().getSouthEast());

        back.setNorthEast(tempCube.getTop().getNorthEast());
        back.setEast(tempCube.getTop().getEast());
        back.setSouthEast(tempCube.getTop().getSouthEast());
    }
}