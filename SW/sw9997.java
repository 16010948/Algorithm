import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int theta = sc.nextInt();
            int hour = (theta * 2) / 60;
            int minute = (theta * 2) % 60;
            System.out.println("#" + test_case + " " + hour + " " + minute);
		}
	}
}