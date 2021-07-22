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
            char[][] farm = new char[n][n];
			for(int i = 0; i < n; i++){
                farm[i] = sc.next().toCharArray();
            }
            int answer = 0;

            for(int i = n / 2; i >= 0; i--) {
                for(int j = 0; j < n; j++) {
                    if(j >= i && j < n - i){
                        answer += farm[(n / 2) - i][j] - '0';
                    }
                }
            }

            for(int i = 1 ; i <= n / 2; i++) {
                for(int j = 0; j < n; j++) {
                    if(j >= i && j < n - i){
                        answer += farm[(n / 2) + i][j] - '0';
                    }
                }
            }

            System.out.println("#" + test_case + " " + answer);
		}
	}
}