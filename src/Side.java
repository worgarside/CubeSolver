// Author: Will Garside
//package

public class Side{
    private char[][] side = new char[3][3];
    private char north;
    private char northEast;
    private char east;
    private char southEast;
    private char south;
    private char southWest;
    private char west;
    private char northWest;
    private char centre;

    public Side(char n, char nE, char e, char sE, char s, char sW, char w, char nW, char c){
        north = n;
        northEast = nE;
        east = e;
        southEast = sE;
        south = s;
        southWest = sW;
        west = w;
        northWest = nW;
        centre = c;
    }

    // Accessor Methods
    public char getNorth(){
        return north;
    }
    public char getNorthEast(){
        return northEast;
    }
    public char getEast(){
        return east;
    }
    public char getSouthEast(){
        return southEast;
    }
    public char getSouth(){
        return south;
    }
    public char getSouthWest(){
        return southWest;
    }
    public char getWest(){
        return west;
    }
    public char getNorthWest(){
        return northWest;
    }
    public char getCentre(){
        return centre;
    }

    public char[][] getSide(){
        side[0][0] = northWest;
        side[0][1] = north;
        side[0][2] = northEast;

        side[1][0] = west;
        side[1][1] = centre;
        side[1][2] = east;

        side[2][0] = southWest;
        side[2][1] = south;
        side[2][2] = southEast;

        return side;
    }
}