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
            int d = sc.nextInt();

            int[] gate = new int[n + 1];
            for(int i = 0; i <n; i++){
            	gate[i] = sc.nextInt();
            }
            gate[n] = 1;

            int count = 0;
            int answer = 0;
            for(int i = 0; i < n + 1; i++) {
            	if(gate[i] == 0) {
                	count++;
                } else {
                	answer += count / d;
                    count = 0;
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}