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
			String tc = sc.next();
            int n = sc.nextInt();

            int[] count = new int[10];
            String[] nums = new String[]{"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"};
            for(int i = 0; i < n; i++) {
            	String num = sc.next();
                for(int j = 0; j < 10; j++) {
                	if(nums[j].equals(num)) {
                    	count[j]++;
                        break;
                    }
                }
            }

            System.out.println(tc);
            for(int i = 0; i < 10; i++) {
            	for(int j = 0; j < count[i]; j++) {
                	System.out.print(" " + nums[i]);
                }
            }
            System.out.println();
		}
	}
}