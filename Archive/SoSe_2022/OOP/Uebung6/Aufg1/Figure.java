abstract class Figure {
    protected float pointX;
    protected float pointY;

    Figure(float pointX, float pointY) {
        this.pointX = pointX;
        this.pointY = pointY;
    }

    Figure(){
        this.pointX = 0;
        this.pointY = 0;
    }

    float getPointX() {
        return pointX;
    }

    float getPointY() {
        return pointY;
    }

    void print() {
        System.out.println("(" + pointX + "|" + pointY+")");
    }
}