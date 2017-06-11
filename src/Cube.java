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

    public void moveX(){
        Cube t = this.copy();

        this.setTop(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setBottom(t.getBack().getSouthEast(), t.getBack().getSouth(), t.getBack().getSouthWest(),
                t.getBack().getEast(), t.getBack().getCentre(), t.getBack().getWest(),
                t.getBack().getNorthEast(), t.getBack().getNorth(), t.getBack().getNorthWest());

        this.setLeft(t.getLeft().getNorthEast(), t.getLeft().getEast(), t.getLeft().getSouthEast(),
                t.getLeft().getNorth(), t.getLeft().getCentre(), t.getLeft().getSouth(),
                t.getLeft().getNorthWest(), t.getLeft().getWest(), t.getLeft().getSouthWest());

        this.setRight(t.getRight().getSouthWest(), t.getRight().getWest(), t.getRight().getNorthWest(),
                t.getRight().getSouth(), t.getRight().getCentre(), t.getRight().getNorth(),
                t.getRight().getSouthEast(), t.getRight().getEast(), t.getRight().getNorthEast());

        this.setFront(t.getBottom().getNorthWest(), t.getBottom().getNorth(), t.getBottom().getNorthEast(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getBottom().getSouthWest(), t.getBottom().getSouth(), t.getBottom().getSouthEast());

        this.setBack(t.getTop().getSouthWest(), t.getTop().getSouth(), t.getTop().getSouthEast(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getTop().getNorthWest(), t.getTop().getNorth(), t.getTop().getNorthEast());
    }

    public void moveNotX(){
        Cube t = this.copy();

        this.setTop(t.getBack().getSouthEast(), t.getBack().getSouth(), t.getBack().getSouthWest(),
                t.getBack().getEast(), t.getBack().getCentre(), t.getBack().getWest(),
                t.getBack().getNorthEast(), t.getBack().getNorth(), t.getBack().getNorthWest());

        this.setBottom(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setLeft(t.getLeft().getSouthWest(), t.getLeft().getWest(), t.getLeft().getNorthWest(),
                t.getLeft().getSouth(), t.getLeft().getCentre(), t.getLeft().getNorth(),
                t.getLeft().getSouthEast(), t.getLeft().getEast(), t.getLeft().getNorthEast());

        this.setRight(t.getRight().getNorthEast(), t.getRight().getEast(), t.getRight().getSouthEast(),
                t.getRight().getNorth(), t.getRight().getCentre(), t.getRight().getSouth(),
                t.getRight().getNorthWest(), t.getRight().getWest(), t.getRight().getSouthWest());

        this.setFront(t.getTop().getNorthWest(), t.getTop().getNorth(), t.getTop().getNorthEast(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getTop().getSouthWest(), t.getTop().getSouth(), t.getTop().getSouthEast());

        this.setBack(t.getBottom().getSouthEast(), t.getBottom().getSouth(), t.getBottom().getSouthWest(),
                t.getBottom().getEast(), t.getBottom().getCentre(), t.getBottom().getWest(),
                t.getBottom().getSouthEast(), t.getBottom().getNorth(), t.getBottom().getNorthWest());
    }

    public void moveY(){
        Cube t = this.copy();

        this.setTop(t.getTop().getSouthWest(), t.getTop().getWest(), t.getTop().getNorthWest(),
                t.getTop().getSouth(), t.getTop().getCentre(), t.getTop().getNorth(),
                t.getTop().getSouthEast(), t.getTop().getEast(), t.getTop().getNorthEast());

        this.setBottom(t.getBottom().getNorthEast(), t.getBottom().getEast(), t.getBottom().getSouthEast(),
                t.getBottom().getNorth(), t.getBottom().getCentre(), t.getBottom().getSouth(),
                t.getBottom().getNorthWest(), t.getBottom().getWest(), t.getBottom().getSouthWest());

        this.setLeft(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setRight(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setFront(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setBack(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());
    }

    public void moveNotY(){
        Cube t = this.copy();

        this.setTop(t.getTop().getNorthEast(), t.getTop().getEast(), t.getTop().getSouthEast(),
                t.getTop().getNorth(), t.getTop().getCentre(), t.getTop().getSouth(),
                t.getTop().getNorthWest(), t.getTop().getWest(), t.getTop().getSouthWest());

        this.setBottom(t.getBottom().getSouthWest(), t.getBottom().getWest(), t.getBottom().getNorthWest(),
                t.getBottom().getSouth(), t.getBottom().getCentre(), t.getBottom().getNorth(),
                t.getBottom().getSouthEast(), t.getBottom().getEast(), t.getBottom().getNorthEast());

        this.setLeft(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setRight(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setFront(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setBack(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());
    }

    public void moveZ(){
        Cube t = this.copy();

        this.setTop(t.getLeft().getSouthWest(), t.getLeft().getWest(), t.getLeft().getNorthWest(),
                t.getLeft().getSouth(), t.getLeft().getCentre(), t.getLeft().getNorth(),
                t.getLeft().getSouthEast(), t.getLeft().getEast(), t.getLeft().getNorthEast());

        this.setBottom(t.getRight().getSouthWest(), t.getRight().getWest(), t.getRight().getNorthWest(),
                t.getRight().getSouth(), t.getRight().getCentre(), t.getRight().getNorth(),
                t.getRight().getSouthEast(), t.getRight().getEast(), t.getRight().getNorthEast());

        this.setLeft(t.getBottom().getSouthWest(), t.getBottom().getWest(), t.getBottom().getNorthWest(),
                t.getBottom().getSouth(), t.getBottom().getCentre(), t.getBottom().getNorth(),
                t.getBottom().getSouthEast(), t.getBottom().getEast(), t.getBottom().getNorthEast());

        this.setRight(t.getTop().getSouthWest(), t.getTop().getWest(), t.getTop().getNorthWest(),
                t.getTop().getSouth(), t.getTop().getCentre(), t.getTop().getNorth(),
                t.getTop().getSouthEast(), t.getTop().getEast(), t.getTop().getNorthEast());

        this.setFront(t.getFront().getSouthWest(), t.getFront().getWest(), t.getFront().getNorthWest(),
                t.getFront().getSouth(), t.getFront().getCentre(), t.getFront().getNorth(),
                t.getFront().getSouthEast(), t.getFront().getEast(), t.getFront().getNorthEast());

        this.setBack(t.getBack().getNorthEast(), t.getBack().getEast(), t.getBack().getSouthEast(),
                t.getBack().getNorth(), t.getBack().getCentre(), t.getBack().getSouth(),
                t.getBack().getNorthWest(), t.getBack().getWest(), t.getBack().getSouthWest());

    }

    public void moveNotZ(){
        Cube t = this.copy();

        this.setTop(t.getRight().getNorthEast(), t.getRight().getEast(), t.getRight().getSouthEast(),
                t.getRight().getNorth(), t.getRight().getCentre(), t.getRight().getSouth(),
                t.getRight().getNorthWest(), t.getRight().getWest(), t.getRight().getSouthWest());

        this.setBottom(t.getLeft().getNorthEast(), t.getLeft().getEast(), t.getLeft().getSouthEast(),
                t.getLeft().getNorth(), t.getLeft().getCentre(), t.getLeft().getSouth(),
                t.getLeft().getNorthWest(), t.getLeft().getWest(), t.getLeft().getSouthWest());

        this.setLeft(t.getTop().getSouthWest(), t.getTop().getWest(), t.getTop().getNorthWest(),
                t.getTop().getSouth(), t.getTop().getCentre(), t.getTop().getNorth(),
                t.getTop().getSouthEast(), t.getTop().getEast(), t.getTop().getNorthEast());

        this.setRight(t.getBottom().getNorthEast(), t.getBottom().getEast(), t.getBottom().getSouthEast(),
                t.getBottom().getNorth(), t.getBottom().getCentre(), t.getBottom().getSouth(),
                t.getBottom().getNorthWest(), t.getBottom().getWest(), t.getBottom().getSouthWest());

        this.setFront(t.getFront().getNorthEast(), t.getFront().getEast(), t.getFront().getSouthEast(),
                t.getFront().getNorth(), t.getFront().getCentre(), t.getFront().getSouth(),
                t.getFront().getNorthWest(), t.getFront().getWest(), t.getFront().getSouthWest());

        this.setBack(t.getBack().getSouthWest(), t.getBack().getWest(), t.getBack().getNorthWest(),
                t.getBack().getSouth(), t.getBack().getCentre(), t.getBack().getNorth(),
                t.getBack().getSouthEast(), t.getBack().getEast(), t.getBack().getNorthEast());
    }

    public void moveR(){
        Cube t = this.copy();

        this.setTop(t.getTop().getNorthWest(), t.getTop().getNorth(), t.getFront().getNorthEast(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getFront().getEast(),
                t.getTop().getSouthWest(), t.getTop().getSouth(), t.getFront().getSouthEast());

        this.setFront(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getBottom().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getBottom().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getBottom().getSouthEast());

        this.setBottom(t.getBottom().getNorthWest(), t.getBottom().getNorth(), t.getBack().getSouthWest(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getBack().getWest(),
                t.getBottom().getSouthWest(), t.getBottom().getSouth(), t.getBack().getNorthWest());

        this.setBack(t.getTop().getSouthEast(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getTop().getEast(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getTop().getNorthEast(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setRight(t.getRight().getSouthWest(), t.getRight().getWest(), t.getRight().getNorthWest(),
                t.getRight().getSouth(), t.getRight().getCentre(), t.getRight().getNorth(),
                t.getRight().getSouthEast(), t.getRight().getEast(), t.getRight().getNorthEast());
    }

    public void moveNotR(){
        Cube t = this.copy();

        this.setTop(t.getTop().getNorthWest(), t.getTop().getNorth(), t.getBack().getSouthWest(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getBack().getWest(),
                t.getTop().getSouthWest(), t.getTop().getSouth(), t.getBack().getNorthWest());

        this.setFront(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getTop().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getTop().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getTop().getSouthEast());

        this.setBottom(t.getBottom().getNorthWest(), t.getBottom().getNorth(), t.getFront().getNorthEast(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getFront().getEast(),
                t.getBottom().getSouthWest(), t.getBottom().getSouth(), t.getFront().getSouthEast());

        this.setBack(t.getBottom().getNorthEast(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getBottom().getEast(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getBottom().getSouthEast(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setRight(t.getRight().getNorthEast(), t.getRight().getEast(), t.getRight().getSouthEast(),
                t.getRight().getNorth(), t.getRight().getCentre(), t.getRight().getSouth(),
                t.getRight().getNorthWest(), t.getRight().getWest(), t.getRight().getSouthWest());
    }

    public void moveL(){
        Cube t = this.copy();

        this.setTop(t.getBack().getSouthEast(), t.getTop().getNorth(), t.getTop().getNorthEast(),
                t.getBack().getEast(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getBack().getNorthEast(), t.getTop().getSouth(), t.getTop().getSouthEast());

        this.setFront(t.getTop().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getTop().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getTop().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setBottom(t.getFront().getNorthWest(), t.getBottom().getNorth(), t.getBottom().getNorthEast(),
                t.getFront().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getFront().getSouthWest(), t.getBottom().getSouth(), t.getBottom().getSouthEast());

        this.setBack(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBottom().getNorthWest(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBottom().getWest(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBottom().getSouthWest());

        this.setLeft(t.getLeft().getSouthWest(), t.getLeft().getWest(), t.getLeft().getNorthWest(),
                t.getLeft().getSouth(), t.getLeft().getCentre(), t.getLeft().getNorth(),
                t.getLeft().getSouthEast(), t.getLeft().getEast(), t.getLeft().getNorthEast());
    }

    public void moveNotL(){
        Cube t = this.copy();

        this.setTop(t.getFront().getNorthWest(), t.getTop().getNorth(), t.getTop().getNorthEast(),
                t.getFront().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getFront().getSouthWest(), t.getTop().getSouth(), t.getTop().getSouthEast());

        this.setFront(t.getBottom().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getBottom().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getBottom().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setBottom(t.getBack().getSouthEast(), t.getBottom().getNorth(), t.getBottom().getNorthEast(),
                t.getBack().getEast(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getBack().getNorthEast(), t.getBottom().getSouth(), t.getBottom().getSouthEast());

        this.setBack(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getTop().getSouthWest(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getTop().getWest(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getTop().getNorthWest());

        this.setLeft(t.getLeft().getNorthEast(), t.getLeft().getEast(), t.getLeft().getSouthEast(),
                t.getLeft().getNorth(), t.getLeft().getCentre(), t.getLeft().getSouth(),
                t.getLeft().getNorthWest(), t.getLeft().getWest(), t.getLeft().getSouthWest());
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
        Cube t = this.copy();

        this.setFront(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setLeft(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setBack(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setRight(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setTop(t.getTop().getSouthWest(), t.getTop().getWest(), t.getTop().getNorthWest(),
                t.getTop().getSouth(), t.getTop().getCentre(), t.getTop().getNorth(),
                t.getTop().getSouthEast(), t.getTop().getEast(), t.getTop().getNorthEast());
    }

    public void moveNotU(){
        Cube t = this.copy();

        this.setFront(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setLeft(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setBack(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setRight(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setTop(t.getTop().getNorthEast(), t.getTop().getEast(), t.getTop().getSouthEast(),
                t.getTop().getNorth(), t.getTop().getCentre(), t.getTop().getSouth(),
                t.getTop().getNorthWest(), t.getTop().getWest(), t.getTop().getSouthWest());
    }

    public void moveD(){
        Cube t = this.copy();

        this.setFront(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setLeft(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setBack(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setRight(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setBottom(t.getBottom().getSouthWest(), t.getBottom().getWest(), t.getBottom().getNorthWest(),
                t.getBottom().getSouth(), t.getBottom().getCentre(), t.getBottom().getNorth(),
                t.getBottom().getSouthEast(), t.getBottom().getEast(), t.getBottom().getNorthEast());
    }

    public void moveNotD(){
        Cube t = this.copy();

        this.setFront(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
                t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setLeft(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

        this.setBack(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
                t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setRight(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

        this.setBottom(t.getBottom().getNorthEast(), t.getBottom().getEast(), t.getBottom().getSouthEast(),
                t.getBottom().getNorth(), t.getBottom().getCentre(), t.getBottom().getSouth(),
                t.getBottom().getNorthWest(), t.getBottom().getWest(), t.getBottom().getSouthWest());
    }

    public void moveU2(){
        this.moveU();
        this.moveU();
    }

    public void moveD2(){
        this.moveD();
        this.moveD();
    }

    public void moveF(){
        Cube t = this.copy();

        this.setTop(t.getTop().getNorthWest(), t.getTop().getNorth(), t.getTop().getNorthEast(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getLeft().getSouthEast(), t.getLeft().getEast(), t.getLeft().getNorthEast());

        this.setBottom(t.getRight().getSouthWest(), t.getRight().getWest(), t.getRight().getNorthWest(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getBottom().getSouthWest(), t.getBottom().getSouth(), t.getBottom().getSouthEast());

        this.setLeft(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getBottom().getNorthWest(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getBottom().getNorth(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getBottom().getNorthEast());

        this.setRight(t.getTop().getSouthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getTop().getSouth(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getTop().getSouthEast(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setFront(t.getFront().getSouthWest(), t.getFront().getWest(), t.getFront().getNorthWest(),
                t.getFront().getSouth(), t.getFront().getCentre(), t.getFront().getNorth(),
                t.getFront().getSouthEast(), t.getFront().getEast(), t.getFront().getNorthEast());
    }

    public void moveNotF(){
        Cube t = this.copy();

        this.setTop(t.getTop().getNorthWest(), t.getTop().getNorth(), t.getTop().getNorthEast(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getRight().getNorthWest(), t.getRight().getWest(), t.getRight().getSouthWest());

        this.setBottom(t.getLeft().getNorthEast(), t.getLeft().getEast(), t.getLeft().getSouthEast(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getBottom().getSouthWest(), t.getBottom().getSouth(), t.getBottom().getSouthEast());

        this.setLeft(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getTop().getSouthEast(),
                t.getLeft().getWest(), t.getLeft().getCentre(), t.getTop().getSouth(),
                t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getTop().getSouthWest());

        this.setRight(t.getBottom().getNorthEast(), t.getRight().getNorth(), t.getRight().getNorthEast(),
                t.getBottom().getNorth(), t.getRight().getCentre(), t.getRight().getEast(),
                t.getBottom().getNorthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

        this.setFront(t.getFront().getNorthEast(), t.getFront().getEast(), t.getFront().getSouthEast(),
                t.getFront().getNorth(), t.getFront().getCentre(), t.getFront().getSouth(),
                t.getFront().getNorthWest(), t.getFront().getWest(), t.getFront().getSouthWest());
    }

    public void moveB(){
        Cube t = this.copy();

        this.setTop(t.getRight().getNorthEast(), t.getRight().getEast(), t.getRight().getSouthEast(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getTop().getSouthWest(), t.getTop().getSouth(), t.getTop().getSouthEast());

        this.setBottom(t.getBottom().getNorthWest(), t.getBottom().getNorth(), t.getBottom().getNorthEast(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getLeft().getNorthWest(), t.getLeft().getWest(), t.getLeft().getSouthWest());

        this.setLeft(t.getTop().getNorthEast(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getTop().getNorth(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getTop().getNorthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setRight(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getBottom().getSouthEast(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getBottom().getSouth(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getBottom().getSouthWest());

        this.setBack(t.getBack().getSouthWest(), t.getBack().getWest(), t.getBack().getNorthWest(),
                t.getBack().getSouth(), t.getBack().getCentre(), t.getBack().getNorth(),
                t.getBack().getSouthEast(), t.getBack().getEast(), t.getBack().getNorthEast());
    }

    public void moveNotB(){
        Cube t = this.copy();

        this.setTop(t.getLeft().getSouthWest(), t.getLeft().getWest(), t.getLeft().getNorthWest(),
                t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
                t.getTop().getSouthWest(), t.getTop().getSouth(), t.getTop().getSouthEast());

        this.setBottom(t.getBottom().getNorthWest(), t.getBottom().getNorth(), t.getBottom().getNorthEast(),
                t.getBottom().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
                t.getRight().getSouthEast(), t.getRight().getEast(), t.getRight().getNorthEast());

        this.setLeft(t.getBottom().getSouthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
                t.getBottom().getSouth(), t.getLeft().getCentre(), t.getLeft().getEast(),
                t.getBottom().getSouthEast(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

        this.setRight(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getTop().getNorthWest(),
                t.getRight().getWest(), t.getRight().getCentre(), t.getTop().getNorth(),
                t.getRight().getSouthWest(), t.getRight().getSouth(), t.getTop().getNorthEast());

        this.setBack(t.getBack().getNorthEast(), t.getBack().getEast(), t.getBack().getSouthEast(),
                t.getBack().getNorth(), t.getBack().getCentre(), t.getBack().getSouth(),
                t.getBack().getNorthWest(), t.getBack().getWest(), t.getBack().getSouthWest());
    }

    public void moveF2(){
        this.moveF();
        this.moveF();
    }

    public void moveB2(){
        this.moveB();
        this.moveB();
    }

    public void moveM(){
        this.moveR();
        this.moveNotL();
        this.moveNotX();
    }

    public void moveNotM(){
        this.moveNotR();
        this.moveL();
        this.moveX();
    }

    public void moveM2(){
        this.moveM();
        this.moveM();
    }

    public void moveE(){
        this.moveU();
        this.moveNotD();
        this.moveNotY();
    }

    public void moveNotE(){
        this.moveNotU();
        this.moveD();
        this.moveY();
    }

    public void moveE2(){
        this.moveE();
        this.moveE();
    }

    public void moveS(){
        this.moveNotF();
        this.moveB();
        this.moveZ();
    }

    public void moveNotS(){
        this.moveF();
        this.moveNotB();
        this.moveNotZ();
    }

    public void moveS2(){
        this.moveS();
        this.moveS();
    }
}



/*

    this.setTop(t.getTop().getNorthWest(), t.getTop().getNorth(), t.getTop().getNorthEast(),
            t.getTop().getWest(), t.getTop().getCentre(), t.getTop().getEast(),
            t.getTop().getSouthWest(), t.getTop().getSouth(), t.getTop().getSouthEast());

    this.setBottom(t.getBottom().getNorthWest(), t.getBottom().getNorth(), t.getBottom().getNorthEast(),
            t.getBottom().getWest(), t.getBottom().getCentre(), t.getBottom().getEast(),
            t.getBottom().getSouthWest(), t.getBottom().getSouth(), t.getBottom().getSouthEast());

    this.setLeft(t.getLeft().getNorthWest(), t.getLeft().getNorth(), t.getLeft().getNorthEast(),
            t.getLeft().getWest(), t.getLeft().getCentre(), t.getLeft().getEast(),
            t.getLeft().getSouthWest(), t.getLeft().getSouth(), t.getLeft().getSouthEast());

    this.setRight(t.getRight().getNorthWest(), t.getRight().getNorth(), t.getRight().getNorthEast(),
            t.getRight().getWest(), t.getRight().getCentre(), t.getRight().getEast(),
            t.getRight().getSouthWest(), t.getRight().getSouth(), t.getRight().getSouthEast());

    this.setFront(t.getFront().getNorthWest(), t.getFront().getNorth(), t.getFront().getNorthEast(),
            t.getFront().getWest(), t.getFront().getCentre(), t.getFront().getEast(),
            t.getFront().getSouthWest(), t.getFront().getSouth(), t.getFront().getSouthEast());

    this.setBack(t.getBack().getNorthWest(), t.getBack().getNorth(), t.getBack().getNorthEast(),
            t.getBack().getWest(), t.getBack().getCentre(), t.getBack().getEast(),
            t.getBack().getSouthWest(), t.getBack().getSouth(), t.getBack().getSouthEast());

 */