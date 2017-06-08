// Author: Will Garside
//package

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
}