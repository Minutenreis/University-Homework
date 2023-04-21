class DIAarray extends DynIntArray {
    
    int[] array = new int[0];

    @Override
    int getElementCount() {
        return array.length;
    }

    @Override
    int getElementAt(int i) {
        if(i<array.length && i>=0) {
            return array[i];
        }
        return 0;
    }

    @Override
    void setElementAt(int i, int e) {
        if(i<array.length && i>=0) {
            array[i] = e;
        }
    }

    @Override
    void add(int e) {
        int[] newArray = new int[array.length+1];
        for(int i=0; i<array.length; i++){
            newArray[i] = array[i];
        }
        newArray[array.length] = e;
        this.array = newArray;
    }

    @Override
    void print() {
        System.out.print("[");
        for(int i=0; i<array.length; i++){
            if(i>0){
                System.out.print(", ");
            }
            System.out.print(array[i]);
        }
        System.out.println("]");
    }
}
