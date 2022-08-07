import java.util.LinkedList;

public class StringMengeImpl extends AbstrakteStringMenge{
    private LinkedList<String> elementList;

    public StringMengeImpl() {
        elementList = new LinkedList<String>();
    }

    public void add(String s){
        if(!elementList.contains(s)){
            elementList.add(s);
        }
    }

    public void remove(String s){
        if(elementList.contains(s)){
            elementList.remove(s);
        }
    }

    public boolean contains(String s){
        return elementList.contains(s);
    }

    public String[] getElements(){
        return elementList.toArray(new String[elementList.size()]);
    }

    public int getSize(){
        return elementList.size();
    }


    
}
