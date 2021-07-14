import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
        int answer = 0;

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int l = sc.nextInt();
            int u = sc.nextInt();
            int x = sc.nextInt();

            if(x < l){
                answer = l - x;
            } else if(x > u) {
                answer = -1;
            } else {
                answer = 0;
            }

            System.out.println("#" + test_case + " " + answer);
		}
	}
}