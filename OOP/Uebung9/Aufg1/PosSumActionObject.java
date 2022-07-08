public class PosSumActionObject implements ActionObject{
    int sum = 0;
    
    public void action(Node n){
        if(n.data instanceof Integer && (int)n.data > 0){
            sum += (int) n.data;
        }
    }
}
