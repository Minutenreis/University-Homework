class Rectangle extends Figure implements MobileObjekt {
    protected float width;
    protected float height;

    Rectangle() {
        super();
        this.width = 0;
        this.height = 0;
    }

    Rectangle(float pointX, float pointY, float width, float height) {
        super(pointX, pointY);
        this.width = width;
        this.height = height;
    }

    float getWidth() {
        return width;
    }

    float getHeight() {
        return height;
    }

    @Override
    void print() {
        System.out.println("(" + pointX + "|" + pointY + ")" + "width: " + width + " height: " + height);
    }

    @Override
    public void move(float x, float y) {
        pointX = x;
        pointY = y;
    }

    @Override
    public void increase(float n) {
        width *= n;
        height *= n;
    }

    @Override
    public void decrease(float n) {
        width /= n;
        height /= n;
    }

    String relativePosition(Rectangle r) {
        if (isDisjointed(r, this)) {
            return "disjoint";
        }

        if (isSame(r, this)) {
            return "same";
        }

        if (isContained(r, this) || isContained(this, r)) {
            return "contained";
        }

        if (isAligned(r, this)) {
            return "aligned";
        }

        return "other";

    }

    float left(Rectangle r) {
        return r.getPointX();
    }

    float right(Rectangle r) {
        return r.getPointX() + r.getWidth();
    }

    float bot(Rectangle r) {
        return r.getPointY();
    }

    float top(Rectangle r) {
        return r.getPointY() + r.getHeight();
    }

    boolean isDisjointed(Rectangle r, Rectangle s) {
        return (left(r) > right(s) || right(r) < left(s)
                || top(r) < bot(s) || bot(r) > top(s));
    }

    boolean isSame(Rectangle r, Rectangle s) {
        return (left(r) == left(s) && right(r) == right(s)
                && top(r) == top(s) && bot(r) == bot(s));
    }

    boolean isContained(Rectangle r, Rectangle s) {
        return (left(r) >= left(s) && right(r) <= right(s)
                && top(r) <= top(s) && bot(r) >= bot(s));
    }

    boolean isAligned(Rectangle r, Rectangle s) {
        return (((left(r) == right(s) || right(r) == left(s))
                && (isInBetweenVertical(r, s) || isInBetweenVertical(s, r)))
                || ((top(r) == bot(s) || bot(r) == top(s))
                        && (isInBetweenHorizontal(r, s) || isInBetweenHorizontal(s, r))));
    }

    boolean isInBetweenHorizontal(Rectangle r, Rectangle s) {
        return (left(r) >= left(s) && left(r) <= right(s)
                || right(r) >= left(s) && right(r) <= right(s));
    }

    boolean isInBetweenVertical(Rectangle r, Rectangle s) {
        return (top(r) >= bot(s) && top(r) <= top(s)
                || bot(r) >= bot(s) && bot(r) <= top(s));
    }

}
