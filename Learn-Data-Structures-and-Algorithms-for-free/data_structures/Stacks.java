import java.util.Stack;

public class Stacks {

    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();
        
        System.out.println(stack.empty());
        System.out.println(stack.size());

        stack.push("Minecraft");
        stack.push("League of Legends");
        stack.push("CS:GO");

        System.out.println(stack.empty());
        System.out.println(stack);

        stack.pop();
        System.out.println(stack);

        System.out.println(stack.peek());
        System.out.println(stack.search("Minecraft"));

    }
}