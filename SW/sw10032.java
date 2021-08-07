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
            int k = sc.nextInt();
            int result = 0;
            if(n %k != 0){
                result = 1;
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}