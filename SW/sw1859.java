import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            long[] stuff = new long[n];
            for(int i = 0; i < n; i++) {
            	stuff[i] = sc.nextInt();
            }

            long profit = 0;
            long max = 0;
            for(int i = n - 1; i >= 0; i--) {
            	if(stuff[i] > max){
                	max = stuff[i];
                }
                profit += max - stuff[i];
            }
            System.out.println("#" + test_case + " " + profit);

		}
	}
}