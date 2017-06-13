public class Side{
    private char northWest;
    private char north;
    private char northEast;
    private char east;
    private char centre;
    private char west;
    private char southEast;
    private char south;
    private char southWest;

    public Side(char nW, char n, char nE, char w, char c, char e, char sE, char s, char sW){
        northWest = nW;
        north = n;
        northEast = nE;
        west = w;
        centre = c;
        east = e;
        southEast = sE;
        south = s;
        southWest = sW;
    }

    // Getter Methods
    public char getNorthWest(){return northWest;}
    public char getNorth(){return north;}
    public char getNorthEast(){return northEast;}
    public char getWest(){return west;}
    public char getCentre(){return centre;}
    public char getEast(){return east;}
    public char getSouthEast(){return southEast;}
    public char getSouth(){return south;}
    public char getSouthWest(){return southWest;}

    public char getCell(int[] loc){
        char[][] tempChar = {{northWest, north, northEast}, {west, centre, east}, {southWest, south, southEast}};
        return tempChar[loc[0]][loc[1]];
    }

    // Setter Methods
    public void setNorthWest(char value){northWest = value;}
    public void setNorth(char value){north = value;}
    public void setNorthEast(char value){northEast = value;}
    public void setWest(char value){west = value;}
    public void setCentre(char value){centre = value;}
    public void setEast(char value){east = value;}
    public void setSouthEast(char value){southEast = value;}
    public void setSouth(char value){south = value;}
    public void setSouthWest(char value){southWest = value;}

    @Override
    public String toString() {
        String result = northWest + "  " + north + "  " + northEast + "\n" + west + "  " + centre + "  " + east + "\n" + southWest + "  " + south + "  " + southEast;
        return result;
    }

    public Side copy(){
        return new Side(northWest, north, northEast, west, centre, east, southEast, south, southWest);
    }
}