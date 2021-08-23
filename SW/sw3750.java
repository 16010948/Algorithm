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
			long n = sc.nextLong();

            int sum = 0;
            while(n > 0){
            	sum += n % 10;
                n /= 10;
                if(n == 0 && sum / 10 > 0) {
                	n = sum;
                    sum = 0;
                }
            }
            System.out.println("#" + test_case + " " + sum);
		}
	}
}