import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static class Histogram {
		int idx;
		int width;

		public Histogram(int idx, int width) {
			this.idx = idx;
			this.width = width;
		}
	}

	static class Stack<E> {
		List<E> data;

		public Stack() {
			this.data = new ArrayList<>();
		}

		void push(E e) {
			data.add(e);
		}

		E pop() {
			E e = peek();
			data.remove(size() - 1);
			return e;
		}

		E peek() {
			return data.get(size() - 1);
		}

		int size() {
			return data.size();
		}

		boolean isEmpty() {
			return data.size() == 0;
		}


	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int[] h = new int[n + 1];
		Stack<Histogram> stack = new Stack();
		int answer = 0;
		for(int i = 0; i < n; i++) {
			h[i] = sc.nextInt();
		}

		for(int i = 0; i <= n; i++) {
			Histogram prev = new Histogram(i, 0);
			while(!stack.isEmpty() && h[stack.peek().idx] > h[i]) {
				prev = stack.pop();
				answer = Math.max(answer, h[prev.idx] * (i - prev.idx + prev.width));
			}
			stack.push(new Histogram(i, i - prev.idx + prev.width));
		}

		System.out.println(answer);
	}

}
