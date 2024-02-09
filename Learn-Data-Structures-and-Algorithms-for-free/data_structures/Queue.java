import java.util.*;

public class Queue {
    public static void main(String[] args) {
        LinkedList<String> queue = new LinkedList<String>();
        queue.offer("Karen");
        queue.offer("Chad");
        queue.offer("Steve");
        queue.offer("Harold");

        System.out.println(queue.peek());
        System.out.println(queue.isEmpty());
        System.out.println(queue.contains("Chad"));

        
        queue.poll();
        queue.poll();
        queue.poll();
        queue.poll();

        System.out.println(queue);
        System.out.println(queue.isEmpty());

    }
}
