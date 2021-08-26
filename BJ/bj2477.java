import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static final int SIDE = 6;
	static final int DIRECTION = 4;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[][] length = new int[SIDE ][2];
		int maxHeight = 0;
		int maxWidth = 0;
		for(int i = 0; i < SIDE; i++) {
			int dir = sc.nextInt();
			int l = sc.nextInt();
			length[i] = new int[] {dir, l};
			if(dir <= 2) {
				maxHeight = Math.max(maxHeight, l);
			} else {
				maxWidth = Math.max(maxWidth, l);
			}
		}

		int removeHeight = 0;
		int removeWidth = 0;
		for(int i = 0; i < SIDE; i++) {
			if(length[i][0] <= 2) {
				if(maxWidth == length[(i + 1) % SIDE][1] + length[(i + 5) % SIDE][1])
					removeHeight = length[i][1];
			} else {
				if(maxHeight == length[(i + 1) % SIDE][1] + length[(i + 5) % SIDE][1])
					removeWidth = length[i][1];

			}
		}
		System.out.println(((maxHeight * maxWidth) - (removeHeight * removeWidth)) * N);
	}
}
