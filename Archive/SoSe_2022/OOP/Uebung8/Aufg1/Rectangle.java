class Rectangle implements ResizeableGO, MoveableGO {
    private float x, y, width, height;
    private int color;
    private boolean visible;

    Rectangle(float x, float y, float width, float height, int color) {
        if (this.width < 0 || this.height < 0) {
            throw new IllegalArgumentException("Width and height must be positive.");
        }
        if (this.color < 0 || this.color > 0xFFFFFF) {
            throw new IllegalArgumentException("Color must be between 0 and 0xFFFFFF.");
        }
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
    }

    public void move(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public void resize(float x) {
        if (x < 0) {
            throw new IllegalArgumentException("Width and height must be positive.");
        }
        this.width = x;
        this.height = x;
    }

    public void setColor(int x) {
        if (this.color < 0 || this.color > 0xFFFFFF) {
            throw new IllegalArgumentException("Color must be between 0 and 0xFFFFFF.");
        }
        this.color = x;
    }

    public void show() {
        this.visible = true;
    }

    public void hide() {
        this.visible = false;
    }

    @Override
    public String toString() {
        return "Rectangle: " + this.x + " " + this.y + " " + this.width + " " + this.height + " " + "000000".substring(Integer.toHexString(this.color).length())+ Integer.toHexString(this.color) + " "
                + this.visible;
    }

}
