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
            int[][] triangle = new int[n][];
            System.out.println("#" + test_case);

            triangle[0] = new int[]{1};
            System.out.println(triangle[0][0]);
            for(int i = 1; i < n; i++) {
                triangle[i] = new int[i + 1];
                for(int j = 0; j <= i; j++) {
                    if(j >= 1) {
                        triangle[i][j] += triangle[i - 1][j - 1];
                    }
                    if(j <= i - 1) {
                        triangle[i][j] += triangle[i - 1][j];
                    }
                    System.out.print(triangle[i][j] + " ");
                }
                System.out.println();
            }
		}
	}
}