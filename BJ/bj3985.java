import java.util.Scanner;

public class Main {
	static int L, N;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		L = sc.nextInt();
		N = sc.nextInt();

		int[] cake = new int[L + 1];
		int maxExpect = 0;
		int maxExpectIndex = 0;
		int maxGet = 0;
		int maxGetIndex = 0;
		for(int i = 1; i <= N; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			int length = end - start + 1;

			if(length > maxExpect) {
				maxExpect = length;
				maxExpectIndex = i;
			}

			int get = 0;
			for(int j = start; j <= end; j++) {
				if(cake[j] == 0) {
					cake[j] = i;
					get++;
				}
			}
			if(get > maxGet) {
				maxGet = get;
				maxGetIndex = i;
			}
		}
		System.out.println(maxExpectIndex);
		System.out.println(maxGetIndex);
	}
}
