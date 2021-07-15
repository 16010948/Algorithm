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
            int[] obstacle = new int[n];
            int increase = 0;
            int decrease = 0;
            for(int i = 0; i < n; i++){
                obstacle[i] = sc.nextInt();
            }

            for(int i = 1; i < n; i++){
                int gap = Math.abs(obstacle[i] - obstacle[i - 1]);
                if(obstacle[i - 1] < obstacle[i] && gap > increase){
                    increase = gap;
                }
                if(obstacle[i - 1] > obstacle[i] && gap > decrease){
                    decrease = gap;
                }
            }
            System.out.println("#" + test_case + " " + increase + " " + decrease);
		}
	}
}