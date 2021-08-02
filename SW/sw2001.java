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
            int m = sc.nextInt();

            int[][] flies = new int[n][n];
           	for(int i = 0; i < n; i++) {
            	for(int j = 0; j < n; j++) {
                	flies[i][j] = sc.nextInt();
                }
            }

            int maxSum = 0;
            for(int i = 0; i <= n - m; i++) {
            	for(int j = 0; j <= n - m; j++) {
                	int sum = 0;
                    for(int k = 0; k < m; k++) {
                    	for(int l = 0; l < m; l++) {
                        	sum += flies[i + k][j + l];
                        }
                    }
                    if(maxSum < sum){
                    	maxSum = sum;
                    }
                }
            }
			System.out.println("#" + test_case + " " +maxSum);
		}
	}
}