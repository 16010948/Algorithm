import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			String[] startTime = sc.next().split(":");
            String[] endTime = sc.next().split(":");

            int[] result = new int[3];
            for(int i = 0; i < 3; i++) {
                result[i] = Integer.parseInt(endTime[i]) - Integer.parseInt(startTime[i]);
            }

            int[] time = {24, 60, 60};
            for(int i = 2; i >= 0; i--) {
                if(result[i] < 0) {
                    result[i] += time[i];
                    if(i > 0){
                    	result[i - 1]--;
                    }
                }
            }

            System.out.print("#" + test_case + " ");
            for(int i = 0; i < 3; i++) {
            	System.out.printf("%02d", result[i]);
                if(i < 3 - 1) {
                	System.out.print(":");
                } else {
                	System.out.println();
                }
            }
		}
	}
}