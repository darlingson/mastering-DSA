public class SpaceComplexity {
    public static void main(String[] args){
        
    }
    public void greet(String[] names){
        String[] copy = new String[names.length];
        for(int i=0; i< names.length; i++){
            System.out.println("Hello " + names[i]);
            copy[i] = names[i];
        }
    }
}
