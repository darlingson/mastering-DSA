public class PrintFirstElement {
    public static void main(String[] args){
        int[] arr = {1,2,3,4};
        printFirstElement(arr);
        log(arr);
    }
    public static void printFirstElement(int[] arr){
        System.out.println(arr[0]);
    }
    public static void log(int[] arr){
        System.out.println();
        for(int number: arr){
            System.out.println(number);
        }
        for(int number: arr){
            System.out.println(number);
        }
    }
    public static void log2(int[] arr){
        System.out.println();
        for(int number: arr){
            for(int number2: arr){
                System.out.println(number2);
                for(int number3: arr){
                    System.out.println(number3);
                }
            }
        }
    }
}