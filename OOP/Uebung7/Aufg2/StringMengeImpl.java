import java.util.LinkedList;

public class StringMengeImpl extends AbstrakteStringMenge{
    private LinkedList<String> elementList;
    private int size;

    public StringMengeImpl() {
        elementList = new LinkedList<String>();
        size = 0;
    }

    public void add(String s){
        if(!elementList.contains(s)){
            elementList.add(s);
            size++;
        }
    }

    public void remove(String s){
        if(elementList.contains(s)){
            elementList.remove(s);
            size--;
        }
    }

    public boolean contains(String s){
        return elementList.contains(s);
    }

    public String[] getElements(){
        return elementList.toArray(new String[elementList.size()]);
    }

    public int getSize(){
        return size;
    }


    
}
