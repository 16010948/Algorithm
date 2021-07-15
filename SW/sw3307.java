import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int[] array = new int[n];
            for(int i = 0; i < n; i++){
                array[i] = sc.nextInt();
            }

            int[] dp = new int[n];
            int max = 0;
            for(int i = 0; i < n; i++){
                dp[i] = 1;
                for (int j = 0; j < i; j++) {
                    if (array[i] > array[j]) {
                    	dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
                max = Math.max(max, dp[i]);
            }
            System.out.println("#" + test_case + " " + max);
		}
	}
}