import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int L = sc.nextInt();

		int[] ball = new int[N];
		int index = 0;
		int count = 0;
		while(true) {
			if(++ball[index] == M) break;

			if(ball[index] % 2 == 1) index = (index + L) % N;
			else {
				index = (N + (index - L)) % N;
			}
			count++;
		}
		System.out.println(count);
	}
}
