import java.util.Scanner;

public class SwitchOnOff {
	static int N;
	static int[] bulb;

	static void invertMultiple(int position) {
		for(int i = 1; i <= (N / position); i++) {
			bulb[position * i] = bulb[position * i] == 0 ? 1 : 0;
		}
	}

	static void invertSymmetry(int position) {
		int left = position - 1;
		int right = position + 1;

		bulb[position] = bulb[position] == 0 ? 1 : 0;
		while(left >= 1 && right <= N && bulb[left] == bulb[right]) {
			bulb[left] = bulb[left] == 0 ? 1 : 0;
			bulb[right] = bulb[right] == 0 ? 1 : 0;
			left--;
			right++;
		}


	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();

		bulb = new int[N + 1];
		for(int i = 1; i <= N; i++) {
			bulb[i] = sc.nextInt();
		}

		int K = sc.nextInt();
		for(int i = 0; i < K; i++) {
			int gender = sc.nextInt();
			int position = sc.nextInt();

			switch(gender) {
				case 1:
					invertMultiple(position);
					break;
				case 2:
					invertSymmetry(position);
					break;
			}
		}

		for(int i = 1; i <= N; i++) {
			System.out.print(bulb[i] + " ");
			if(i % 20 == 0) {
				System.out.println();
			}
		}
	}
}
