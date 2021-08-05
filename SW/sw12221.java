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
            int a = sc.nextInt();
            int b = sc.nextInt();

            int result;
            if(a >= 10 || b >= 10) {
            	result = -1;
            } else {
                result = a * b;
            }

            System.out.println("#" + test_case + " " + result);
		}
	}
}