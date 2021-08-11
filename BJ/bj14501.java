import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] period = new int[n];
		int[] profit = new int[n];
		for(int i = 0; i < n; i++) {
			period[i] = sc.nextInt();
			profit[i] = sc.nextInt();
		}

		int[] dp = new int[n + 1];
		for(int i = n - 1; i >= 0; i--) {
			if(period[i] + i > n) {
				dp[i] = dp[i + 1];
			} else {
				dp[i] = Math.max(dp[i + 1], profit[i] + dp[i + period[i]]);
			}
		}

		System.out.println(dp[0]);
	}
}
