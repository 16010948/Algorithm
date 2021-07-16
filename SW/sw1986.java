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
            int (n % 2 == 0) ? n / 2 * -1 : n / 2  + 1;
            System.out.println("#" + test_case + " " + (oddSum - evenSum));
		}
	}
}