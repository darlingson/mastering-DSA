import java.util.NoSuchElementException;

public class LinkedList {
    private class Node {
        private int value;
        private Node next;

        public Node(int value) {
            this.value = value;
        }
    }
    private Node first;
    private Node last;

    public void addLast(int item) {
        Node node = new Node(item);

        if (isEmpty()) {
            first = node;
            last = node;
        }
        else {
            last.next = node;
            last = node;
        }
    }
    public void addFirst(int item) {
        Node node = new Node(item);

        if (isEmpty()) {
            first = node;
            last = node;
        }
        else {
            node.next = first;
            first = node;
        }
   }
   public int indexOf(int item) {
    int index = 0;
    var current = first;

    while (current != null) {
        if (current.value == item) {
            return index;
        }
        current = current.next;
        index++;
    }
    return -1;
   }
   public boolean contains(int item) {
    return indexOf(item) != -1;
   }
   public void removeFirst() {
    if (isEmpty()) {
        throw new NoSuchElementException();
    }
    if(first == last) {
        first = last = null;
        return;
    }
    var second = first.next;
    first.next = null;
    first = second;
   }
   public void removeLast() {
    if (isEmpty()) {
        throw new NoSuchElementException();
    }
    if(first == last) {
        first = last = null;
        return;
    }
    var previous = getPrevios(last);
    last = previous;
    last.next = null;
   }
   private Node getPrevios(Node node) {
    var current = first;
    while (current != null) {
     if (current.next == node) return current;
     current = current.next;
    }
    return null;
   }
   private boolean isEmpty() {
    return first == null;
   }
}
 