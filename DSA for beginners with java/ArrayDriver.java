public class ArrayDriver {
    public static void main(String[] args) {
        Array numbers = new Array(2);
        numbers.insert(10);
        numbers.insert(20);
        numbers.insert(30);
        numbers.insert(40);
        System.out.println(numbers.indexOf(10));
        numbers.print();
    }
}
