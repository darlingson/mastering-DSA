import java.util.Arrays;

public class WorkingWithArrays {
    public static void main(String[] args) {
        int[] numbers = new int[3];
        System.out.println(Arrays.toString(numbers));

        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        System.out.println(Arrays.toString(numbers));

        int[] numbers2 = {10, 20, 30};
        System.out.println(Arrays.toString(numbers2));
        System.out.println(numbers2.length);
    }
}
