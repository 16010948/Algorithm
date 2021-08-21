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
			double a = sc.nextDouble();
            double b = sc.nextDouble();
            double c = sc.nextDouble();
            double d = sc.nextDouble();

            String result;
            if( a / b == c / d) {
            	result = "DRAW";
            } else if(a / b > c / d) {
            	result = "ALICE";
            } else {
            	result = "BOB";
            }

            System.out.println("#" + test_case + " " + result);
		}
	}
}