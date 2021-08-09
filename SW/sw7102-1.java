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
            int m = sc.nextInt();

            int[] count = new int[n + m + 1];
            int max = 0;

            for(int i = 1; i <= n; i++) {
            	for(int j = 1; j <= m; j++) {
                	count[i + j]++;
                    if(count[i + j] > max) {
                    	max = count[i + j];
                    }
                }
            }

			System.out.print("#" + test_case);
            for(int i = 2; i < n + m + 1; i++) {
            	if(count[i] == max){
                	System.out.print(" " + i);
                }
            }
            System.out.println();
		}
	}
}