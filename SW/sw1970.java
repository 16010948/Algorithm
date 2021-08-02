import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        final int[] unit = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
            int money = sc.nextInt();
            System.out.println("#" + test_case);
            for(int i = 0; i < unit.length; i++) {
            	System.out.print((money / unit[i]) + " ");
                money %= unit[i];
            }
            System.out.println();
		}
	}
}