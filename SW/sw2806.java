import java.util.Scanner;

class Solution
{
    static int[] chess;
    static int count;
    static int N;

    static boolean isPossible(int col) {
    	for(int i = 0; i < col; i++) {
        	if(chess[col] == chess[i] || Math.abs(col - i) == Math.abs(chess[col] - chess[i])) {
            	return false;
            }
        }
        return true;
    }

    static void nQueen(int depth) {
    	if(depth == N) {
        	count++;
            return;
        }

        for(int i = 0; i < N; i++) {
        	chess[depth] = i;
            if(isPossible(depth)) {
            	nQueen(depth + 1);
            }
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
            chess = new int[N];

            count = 0;
            nQueen(0);
            System.out.println("#" + test_case + " " + count);

		}
	}
}