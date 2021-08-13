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
			double D = sc.nextDouble();
            int L = sc.nextInt();
            int N = sc.nextInt();

            System.out.println("#" + test_case + " " + (int)(N * D + D * L * N * (N - 1) / 200));
		}
	}
}