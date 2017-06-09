public class Side{
//    private char[][] side = new char[3][3];
    private char northWest;
    private char north;
    private char northEast;
    private char east;
    private char southEast;
    private char south;
    private char southWest;
    private char west;
    private char centre;

    public Side(char n, char nE, char e, char sE, char s, char sW, char w, char nW, char c){
        northWest = nW;
        north = n;
        northEast = nE;
        east = e;
        southEast = sE;
        south = s;
        southWest = sW;
        west = w;
        centre = c;
    }

    // Getter Methods
    public char getNorthWest(){
        return northWest;
    }
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
    public char getCentre(){
        return centre;
    }
    public char getCell(int[] loc){
        char[][] tempChar = {{northWest, north, northEast}, {west, centre, east}, {southWest, south, southEast}};
        return tempChar[loc[0]][loc[1]];
    }

    // Setter Methods
    public void setNorthWest(char value){
        this.northWest = value;
    }
    public void setNorth(char value){
        this.north = value;
    }
    public void setNorthEast(char value){
        this.northEast = value;
    }
    public void setEast(char value){
        this.east = value;
    }
    public void setSouthEast(char value){
        this.southEast = value;
    }
    public void setSouth(char value){
        this.south = value;
    }
    public void setSouthWest(char value){
        this.southWest = value;
    }
    public void setWest(char value){
        this.west = value;
    }
    public void setCentre(char value){
        this.centre = value;
    }
//    public char setCell(int[] loc, char value){
//        char[][] tempChar = {{northWest, north, northEast}, {west, centre, east}, {southWest, south, southEast}};
//        return tempChar[loc[0]][loc[1]];
//    }

    @Override
    public String toString() {
        String result = northWest + "  " + north + "  " + northEast + "\n" + west + "  " + centre + "  " + east + "\n" + southWest + "  " + south + "  " + southEast;
        return result;
    }

}