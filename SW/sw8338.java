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
			int n = sc.nextInt();
            int[] nums = new int[n];
            for(int i = 0; i < n; i++) {
            	nums[i] = sc.nextInt();
            }

            int result = 0;
            for(int i = 0 ; i < n; i++) {
            	if(result <= 1 || nums[i] <= 1) {
                	result += nums[i];
                } else {
                    result *= nums[i];
                }
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}