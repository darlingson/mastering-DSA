import java.util.LinkedList;

public class LinkedLists {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.add(10);
        list.add(20);
        list.addFirst(30);
        list.addLast(40);
        System.out.println(list.contains(20));

        System.out.println(list);
    }
}
