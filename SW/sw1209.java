import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = 10;

        for(int test_case = 1; test_case <= T; test_case++)
		{
            int tc = sc.nextInt();
            int[][] arr = new int[100][100];
			for(int i = 0; i < 100; i++) {
                for(int j = 0; j < 100; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            int maxSum = 0;
            for(int i = 0; i < 100; i++) {
                int rowSum = 0;
                int colSum = 0;
                for(int j = 0; j < 100; j++) {
                    rowSum += arr[i][j];
                    colSum += arr[j][i];
                }
                maxSum = Math.max(maxSum, Math.max(rowSum, colSum));
            }

            int diaSum = 0;
            int reverseSum = 0;
            for(int i = 0; i < 100; i++) {
                diaSum += arr[i][i];
                reverseSum += arr[i][100 - i - 1];
            }
            maxSum = Math.max(maxSum, Math.max(diaSum, reverseSum));
            System.out.println("#" + tc + " " + maxSum);
		}
	}
}