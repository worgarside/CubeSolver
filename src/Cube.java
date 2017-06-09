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

    // Getter Methods
    public Side getTop(){return top;}
    public Side getLeft(){return left;}
    public Side getRight(){return right;}
    public Side getBottom(){return bottom;}
    public Side getFront(){return front;}
    public Side getBack(){return back;}

    // Setter Methods
    public void setTop(char nW, char n, char nE, char w, char c, char e, char sW, char s, char sE){
        top = new Side(nW, n, nE, w, c, e, sE,s, sW);
    }
    public void setBottom(char nW, char n, char nE, char w, char c, char e, char sW, char s, char sE){
        bottom = new Side(nW, n, nE, w, c, e, sE,s, sW);
    }
    public void setLeft(char nW, char n, char nE, char w, char c, char e, char sW, char s, char sE){
        left = new Side(nW, n, nE, w, c, e, sE,s, sW);
    }
    public void setRight(char nW, char n, char nE, char w, char c, char e, char sW, char s, char sE){
        right = new Side(nW, n, nE, w, c, e, sE,s, sW);
    }
    public void setFront(char nW, char n, char nE, char w, char c, char e, char sW, char s, char sE){
        front = new Side(nW, n, nE, w, c, e, sE,s, sW);
    }
    public void setBack(char nW, char n, char nE, char w, char c, char e, char sW, char s, char sE){
        back = new Side(nW, n, nE, w, c, e, sE,s, sW);
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

    public Cube copy(){
        return new Cube(top, bottom, left, right, front, back);
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
        Cube tempCube = this.copy();

        this.setTop(tempCube.getTop().getNorthWest(), tempCube.getTop().getNorth(), tempCube.getFront().getNorthEast(),
                tempCube.getTop().getWest(), tempCube.getTop().getCentre(), tempCube.getFront().getEast(),
                tempCube.getTop().getSouthWest(), tempCube.getTop().getSouth(), tempCube.getFront().getSouthEast());

        this.setFront(tempCube.getFront().getNorthWest(), tempCube.getFront().getNorth(), tempCube.getBottom().getNorthEast(),
                tempCube.getFront().getWest(), tempCube.getFront().getCentre(), tempCube.getBottom().getEast(),
                tempCube.getFront().getSouthWest(), tempCube.getFront().getSouth(), tempCube.getBottom().getSouthEast());

        this.setBottom(tempCube.getBottom().getNorthWest(), tempCube.getBottom().getNorth(), tempCube.getBack().getSouthWest(),
                tempCube.getBottom().getWest(), tempCube.getBottom().getCentre(), tempCube.getBack().getWest(),
                tempCube.getBottom().getSouthWest(), tempCube.getBottom().getSouth(), tempCube.getBack().getNorthWest());

        this.setBack(tempCube.getTop().getSouthEast(), tempCube.getBack().getNorth(), tempCube.getBack().getNorthEast(),
                tempCube.getTop().getEast(), tempCube.getBack().getCentre(), tempCube.getBack().getEast(),
                tempCube.getTop().getNorthEast(), tempCube.getBack().getSouth(), tempCube.getBack().getSouthEast());

        this.setRight(tempCube.getRight().getSouthWest(), tempCube.getRight().getWest(), tempCube.getRight().getNorthWest(),
                tempCube.getRight().getSouth(), tempCube.getRight().getCentre(), tempCube.getRight().getNorth(),
                tempCube.getRight().getSouthEast(), tempCube.getRight().getEast(), tempCube.getRight().getNorthEast());
    }

    public void moveNotR(){
        Cube tempCube = this.copy();

        this.setTop(tempCube.getTop().getNorthWest(), tempCube.getTop().getNorth(), tempCube.getBack().getSouthWest(),
                tempCube.getTop().getWest(), tempCube.getTop().getCentre(), tempCube.getBack().getWest(),
                tempCube.getTop().getSouthWest(), tempCube.getTop().getSouth(), tempCube.getBack().getNorthWest());

        this.setFront(tempCube.getFront().getNorthWest(), tempCube.getFront().getNorth(), tempCube.getTop().getNorthEast(),
                tempCube.getFront().getWest(), tempCube.getFront().getCentre(), tempCube.getTop().getEast(),
                tempCube.getFront().getSouthWest(), tempCube.getFront().getSouth(), tempCube.getTop().getSouthEast());

        this.setBottom(tempCube.getBottom().getNorthWest(), tempCube.getBottom().getNorth(), tempCube.getFront().getNorthEast(),
                tempCube.getBottom().getWest(), tempCube.getBottom().getCentre(), tempCube.getFront().getEast(),
                tempCube.getBottom().getSouthWest(), tempCube.getBottom().getSouth(), tempCube.getFront().getSouthEast());

        this.setBack(tempCube.getBottom().getNorthEast(), tempCube.getBack().getNorth(), tempCube.getBack().getNorthEast(),
                tempCube.getBottom().getEast(), tempCube.getBack().getCentre(), tempCube.getBack().getEast(),
                tempCube.getBottom().getSouthEast(), tempCube.getBack().getSouth(), tempCube.getBack().getSouthEast());

        this.setRight(tempCube.getRight().getNorthEast(), tempCube.getRight().getEast(), tempCube.getRight().getSouthEast(),
                tempCube.getRight().getNorth(), tempCube.getRight().getCentre(), tempCube.getRight().getSouth(),
                tempCube.getRight().getNorthWest(), tempCube.getRight().getWest(), tempCube.getRight().getSouthWest());
    }

    public void moveL(){
        Cube tempCube = this.copy();

        this.setTop(tempCube.getBack().getSouthEast(), tempCube.getTop().getNorth(), tempCube.getTop().getNorthEast(),
                tempCube.getBack().getEast(), tempCube.getTop().getCentre(), tempCube.getTop().getEast(),
                tempCube.getBack().getNorthEast(), tempCube.getTop().getSouth(), tempCube.getTop().getSouthEast());

        this.setFront(tempCube.getTop().getNorthWest(), tempCube.getFront().getNorth(), tempCube.getFront().getNorthEast(),
                tempCube.getTop().getWest(), tempCube.getFront().getCentre(), tempCube.getFront().getEast(),
                tempCube.getTop().getSouthWest(), tempCube.getFront().getSouth(), tempCube.getFront().getSouthEast());

        this.setBottom(tempCube.getFront().getNorthWest(), tempCube.getBottom().getNorth(), tempCube.getBottom().getNorthEast(),
                tempCube.getFront().getWest(), tempCube.getBottom().getCentre(), tempCube.getBottom().getEast(),
                tempCube.getFront().getSouthWest(), tempCube.getBottom().getSouth(), tempCube.getBottom().getSouthEast());

        this.setBack(tempCube.getBack().getNorthWest(), tempCube.getBack().getNorth(), tempCube.getBottom().getNorthWest(),
                tempCube.getBack().getWest(), tempCube.getBack().getCentre(), tempCube.getBottom().getWest(),
                tempCube.getBack().getSouthWest(), tempCube.getBack().getSouth(), tempCube.getBottom().getSouthWest());

        this.setLeft(tempCube.getLeft().getSouthWest(), tempCube.getLeft().getWest(), tempCube.getLeft().getNorthWest(),
                tempCube.getLeft().getSouth(), tempCube.getLeft().getCentre(), tempCube.getLeft().getNorth(),
                tempCube.getLeft().getSouthEast(), tempCube.getLeft().getEast(), tempCube.getLeft().getNorthEast());
    }

    public void moveNotL(){
        Cube tempCube = this.copy();

        this.setTop(tempCube.getFront().getNorthWest(), tempCube.getTop().getNorth(), tempCube.getTop().getNorthEast(),
                tempCube.getFront().getWest(), tempCube.getTop().getCentre(), tempCube.getTop().getEast(),
                tempCube.getFront().getSouthWest(), tempCube.getTop().getSouth(), tempCube.getTop().getSouthEast());

        this.setFront(tempCube.getBottom().getNorthWest(), tempCube.getFront().getNorth(), tempCube.getFront().getNorthEast(),
                tempCube.getBottom().getWest(), tempCube.getFront().getCentre(), tempCube.getFront().getEast(),
                tempCube.getBottom().getSouthWest(), tempCube.getFront().getSouth(), tempCube.getFront().getSouthEast());

        this.setBottom(tempCube.getBack().getSouthEast(), tempCube.getBottom().getNorth(), tempCube.getBottom().getNorthEast(),
                tempCube.getBack().getEast(), tempCube.getBottom().getCentre(), tempCube.getBottom().getEast(),
                tempCube.getBack().getNorthEast(), tempCube.getBottom().getSouth(), tempCube.getBottom().getSouthEast());

        this.setBack(tempCube.getBack().getNorthWest(), tempCube.getBack().getNorth(), tempCube.getTop().getSouthWest(),
                tempCube.getBack().getWest(), tempCube.getBack().getCentre(), tempCube.getTop().getWest(),
                tempCube.getBack().getSouthWest(), tempCube.getBack().getSouth(), tempCube.getTop().getNorthWest());

        this.setLeft(tempCube.getLeft().getNorthEast(), tempCube.getLeft().getEast(), tempCube.getLeft().getSouthEast(),
                tempCube.getLeft().getNorth(), tempCube.getLeft().getCentre(), tempCube.getLeft().getSouth(),
                tempCube.getLeft().getNorthWest(), tempCube.getLeft().getWest(), tempCube.getLeft().getSouthWest());
    }

    public void moveR2(){
        this.moveR();
        this.moveR();
    }

    public void moveL2(){
        this.moveL();
        this.moveL();
    }

    public void moveU(){
        Cube tempCube = this.copy();

        this.setFront(tempCube.getRight().getNorthWest(), tempCube.getRight().getNorth(), tempCube.getRight().getNorthEast(),
                tempCube.getFront().getWest(), tempCube.getFront().getCentre(), tempCube.getFront().getEast(),
                tempCube.getFront().getSouthWest(), tempCube.getFront().getSouth(), tempCube.getFront().getSouthEast());

        this.setLeft(tempCube.getFront().getNorthWest(), tempCube.getFront().getNorth(), tempCube.getFront().getNorthEast(),
                tempCube.getLeft().getWest(), tempCube.getLeft().getCentre(), tempCube.getLeft().getEast(),
                tempCube.getLeft().getSouthWest(), tempCube.getLeft().getSouth(), tempCube.getLeft().getSouthEast());

        this.setBack(tempCube.getLeft().getNorthWest(), tempCube.getLeft().getNorth(), tempCube.getLeft().getNorthEast(),
                tempCube.getBack().getWest(), tempCube.getBack().getCentre(), tempCube.getBack().getEast(),
                tempCube.getBack().getSouthWest(), tempCube.getBack().getSouth(), tempCube.getBack().getSouthEast());

        this.setRight(tempCube.getBack().getNorthWest(), tempCube.getBack().getNorth(), tempCube.getBack().getNorthEast(),
                tempCube.getRight().getWest(), tempCube.getRight().getCentre(), tempCube.getRight().getEast(),
                tempCube.getRight().getSouthWest(), tempCube.getRight().getSouth(), tempCube.getRight().getSouthEast());

        this.setTop(tempCube.getTop().getSouthWest(), tempCube.getTop().getWest(), tempCube.getTop().getNorthWest(),
                tempCube.getTop().getSouth(), tempCube.getTop().getCentre(), tempCube.getTop().getNorth(),
                tempCube.getTop().getSouthEast(), tempCube.getTop().getEast(), tempCube.getTop().getNorthEast());
    }

    public void moveNotU(){
        Cube tempCube = this.copy();
    }

    public void moveD(){
        Cube tempCube = this.copy();
    }

    public void moveNotD(){
        Cube tempCube = this.copy();
    }

    public void moveU2(){
        Cube tempCube = this.copy();
    }

    public void moveD2(){
        Cube tempCube = this.copy();
    }

    public void moveF(){
        Cube tempCube = this.copy();
    }

    public void moveNotF(){
        Cube tempCube = this.copy();
    }

    public void moveB(){
        Cube tempCube = this.copy();
    }

    public void moveNotB(){
        Cube tempCube = this.copy();
    }

    public void moveF2(){
        Cube tempCube = this.copy();
    }

    public void moveB2(){
        Cube tempCube = this.copy();
    }

    public void moveM(){
        Cube tempCube = this.copy();
    }

    public void moveNotM(){
        Cube tempCube = this.copy();
    }

    public void moveM2(){
        Cube tempCube = this.copy();
    }

    public void moveE(){
        Cube tempCube = this.copy();
    }

    public void moveNotE(){
        Cube tempCube = this.copy();
    }

    public void moveE2(){
        Cube tempCube = this.copy();
    }

    public void moveS(){
        Cube tempCube = this.copy();
    }

    public void moveNotS(){
        Cube tempCube = this.copy();
    }

    public void moveS2(){
        Cube tempCube = this.copy();
    }

    public void moveX(){
        Cube tempCube = this.copy();
    }

    public void moveNotX(){
        Cube tempCube = this.copy();
    }

    public void moveY(){
        Cube tempCube = this.copy();
    }

    public void moveNotY(){
        Cube tempCube = this.copy();
    }

    public void moveZ(){
        Cube tempCube = this.copy();
    }

    public void moveNotZ(){
        Cube tempCube = this.copy();
    }


}