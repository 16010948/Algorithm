import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();

		List<Integer> Josephus = new ArrayList<>();
		for(int i = 1; i <= n; i++) {
			Josephus.add(i);
		}

		int[] result = new int[n];
		int index = 0;
		for(int i = 0; i < n; i++) {
			index = (index + k - 1) % Josephus.size();
			result[i] = Josephus.get(index);
			Josephus.remove(index);
		}

		StringBuilder sb = new StringBuilder();
		sb.append("<");
		for(int r: result) {
			sb.append(r).append(", ");
		}
		sb.setLength(sb.length() - 2);
		sb.append(">");

		System.out.println(sb.toString());
	}
}
