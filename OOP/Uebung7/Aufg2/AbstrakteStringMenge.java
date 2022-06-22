abstract class AbstrakteStringMenge implements StringMenge {

    public int getCharCount() {
        String[] elements = getElements();
        int count = 0;
        for (String s : elements) {
            count += s.length();
        }
        return count;
    }

    public boolean isEmpty() {
        String[] elements = getElements();
        return elements.length == 0;
    }

    public void print(){
        String[] elements = getElements();
        for (String s : elements) {
            System.out.print(s + " ");
        }
        System.out.println();
    }
}
