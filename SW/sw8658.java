import java.util.Scanner;

class Solution
{
    static int digitSum (int n) {
    	int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{

            int maxSum = 0;
            int minSum = 1000001;
			for (int i = 0; i < 10; i++){
                int n = sc.nextInt();
                int sum = digitSum(n);
                minSum = Math.min(minSum, sum);
                maxSum = Math.max(maxSum, sum);
            }

            System.out.println("#" + test_case +" " + maxSum + " " + minSum);

		}
	}
}