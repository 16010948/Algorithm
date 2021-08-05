import java.util.LinkedList;
import java.util.Scanner;

class CardQueue {
	private LinkedList<Integer> data;

	public CardQueue(int n) {
		data = new LinkedList<>();
		for(int i = 1; i <= n; i++) {
			data.add(i);
		}
	}

	public void offer(int card) {
		data.add(card);
	}

	public int size() {
		return data.size();
	}

	public int poll() {
		int card = data.get(0);
		data.removeFirst();
		return card;
	}

	public int peek() {
		return data.get(this.size() - 1);
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n  = sc.nextInt();
		CardQueue queue = new CardQueue(n);

		while(queue.size() > 1) {
			queue.poll();
			queue.offer(queue.poll());
		}

		System.out.println(queue.peek());
	}
}
