import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int n = Integer.parseInt(in.readLine());
		int[] top = new int[n];
		st = new StringTokenizer(in.readLine(), " ");
		for(int i = 0; i < n; i++) {
			top[i] = Integer.parseInt(st.nextToken());
		}

		Stack<Integer> stack = new Stack<>();
		for(int i = 0; i < n; i++) {
			while(!stack.isEmpty() && top[stack.peek() - 1] < top[i]) {
				stack.pop();
			}

			System.out.print((stack.isEmpty() ? 0 : stack.peek()) + " ");
			stack.push(i + 1);
		}
	}
}
