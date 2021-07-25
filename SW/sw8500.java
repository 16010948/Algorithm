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
            int max = 0;
            int answer = 0;
            for(int i = 0; i < n; i++) {
                int seat = sc.nextInt();
                if(max < seat) {
                    max = seat;
                }
                answer += seat + 1;
            }
            answer += max;
            System.out.println("#" + test_case + " " + answer);
		}
	}
}