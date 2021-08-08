import java.util.Scanner;

class Solution
{
    static int n;
    static int m;
    static int[] snack;
    static int answer;

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			n = sc.nextInt();
            m = sc.nextInt();
            snack = new int[n];
            for(int i = 0; i < n; i++) {
            	snack[i] = sc.nextInt();
            }

            answer = 0;
            for(int i = 0; i < n; i++) {
            	for(int j = i + 1; j < n; j++) {
                    int sum = snack[i] + snack[j];
                	if(sum <=m && sum > answer) {
                    	answer = sum;
                    }
                }
            }
            answer = answer == 0? -1 : answer;
            System.out.println("#" + test_case + " " + answer);
		}
	}
}