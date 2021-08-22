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
			long n = sc.nextInt();
            long start = 2 * n * n  - 4 * n + 3;
            long end = start + 2 * 2 * (n - 1);
            System.out.println("#" + test_case + " " +  start + " " + end);
		}
	}
}