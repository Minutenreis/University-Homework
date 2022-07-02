public class PosSumActionObject implements ActionObject{
    int sum = 0;
    
    public void action(Node n){
        if(Integer.class.isInstance(n.data) && (int)n.data > 0){
            sum += (int) n.data;
        }
    }
}
