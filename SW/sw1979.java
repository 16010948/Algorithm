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
            int k = sc.nextInt();
            int[][] puzzle = new int[n + 1][n + 1];

            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    puzzle[i][j] = sc.nextInt();
                }
            }

            int answer = 0;
            for(int i = 0; i < n + 1; i++) {
                int row = 0;
                int col = 0;
                for(int j = 0; j < n + 1; j++) {
                    if(puzzle[i][j] == 0) {
                        if(row == k) {
                            answer++;
                        }
                        row = 0;
                    } else {
                        row++;
                    }

                    if(puzzle[j][i] == 0) {
                        if(col == k) {
                            answer++;
                        }
                        col = 0;
                    } else {
                        col++;
                    }
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}