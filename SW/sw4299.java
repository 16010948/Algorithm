import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		final int PEPERO = 11;
        int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int d = sc.nextInt();
            int h = sc.nextInt();
            int m = sc.nextInt();
            int total = Math.max((d - PEPERO) * 24 * 60 + (h - PEPERO) * 60 + (m - PEPERO), -1);

            System.out.println("#" + test_case + " " + total);
		}
	}
}