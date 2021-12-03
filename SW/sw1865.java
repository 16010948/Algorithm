import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    static int N;
    static boolean[] visited;
    static int[][] percent;
    static double answer;

    static void run(int idx, double total) {
    	if(total <= answer) {
        	return ;
        }

        if(idx == N) {
            answer = total;
            return;
        }

        for(int i = 0; i < N; i++) {
        	if(!visited[i]) {
            	visited[i] = true;
                run(idx + 1, total * percent[idx][i] * 0.01);
                visited[i] = false;
            }
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();

            percent = new int[N][N];
            for(int i = 0; i < N; i++) {
            	for(int j = 0; j < N; j++) {
                	percent[i][j] = sc.nextInt();
                }
            }
            visited = new boolean[N];
            answer = -100;
            run(0, 1);
            System.out.printf("#%d %.6f%n",test_case, answer * 100);
		}
	}
}