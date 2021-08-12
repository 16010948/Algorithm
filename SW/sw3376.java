import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            long[] dp = new long[Math.max(5, n + 1)];

            dp[1] = dp[2] = dp[3] = 1;
            dp[4] = 2;
            for(int i = 5; i <= n; i++) {
				dp[i] = dp[i - 5] + dp[i - 4] + dp[i - 3];
            }
            System.out.println("#" + test_case + " " + dp[n]);

		}
	}
}