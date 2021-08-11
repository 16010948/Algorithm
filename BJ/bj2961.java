import java.util.Scanner;

class Solution {
	static int N;
	static int[] sour;
	static int[] bitter;
	static int min;

	static void powerSet(int idx, int totalSour, int totalBitter) {
		if(idx == N) {
			int gap = Math.abs(totalSour - totalBitter);
			if(gap < min && totalBitter != 0) {
				min = gap;
			}
			return ;
		}

		powerSet(idx + 1, totalSour * sour[idx], totalBitter + bitter[idx]);
		powerSet(idx + 1, totalSour, totalBitter);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();

		sour = new int[N];
		bitter = new int[N];
		for(int i = 0; i < N; i++) {
			sour[i] = sc.nextInt();
			bitter[i] = sc.nextInt();
		}

		min = Integer.MAX_VALUE;
		powerSet(0, 1, 0);
		System.out.println(min);
	}
}
