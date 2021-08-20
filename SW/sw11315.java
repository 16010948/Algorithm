import java.util.Scanner;

class Solution
{
    static int N;
    static char[][] panel;
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
            panel = new char[N][N];
            for(int i = 0; i < N; i++) {
            	panel[i] = sc.next().toCharArray();
            }

            String result = "NO";
            outer: for(int i = 0; i < N; i++) {
            	for(int j = 0; j < N; j++) {
                	if(panel[i][j] == 'o' && isSequence(i, j)) {
                        result = "YES";
                        break outer;
                    }
                }
            }
            System.out.println("#" + test_case + " " + result);
		}
	}

    private static boolean isSequence(int r, int c) {
    	int vertical = 1;
        int horizon = 1;
        int diagonal = 1;
        int reverseDiagonal = 1;

        for(int i = 1; i < 5; i++) {
            if(r + i < N && panel[r + i][c] == 'o') vertical++;
        	if(c + i < N && panel[r][c + i] == 'o') horizon++;
            if(r + i < N &&  c + i < N && panel[r + i][c + i] == 'o') diagonal++;
            if(r - i >= 0 &&  c + i < N && panel[r - i][c + i] == 'o') reverseDiagonal++;
        }
        return vertical == 5 || horizon == 5 || diagonal == 5 || reverseDiagonal == 5;
    }
}