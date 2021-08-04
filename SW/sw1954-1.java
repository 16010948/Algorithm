import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
        int[][] deltas = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int[][] snail = new int[n][n];

            int count = 1;
            int x = -1;
            int y = 0;
            int index = 0;
            while(count <= n * n) {
                int ny = y + deltas[index][0];
                int nx = x + deltas[index][1];
                if(ny < 0 || ny >= n || nx < 0 || nx >= n || snail[ny][nx] != 0) {
                    index = (++index ) % deltas.length;
                } else {
                	y = ny;
                    x = nx;
                    snail[y][x] = count++;
                }
            }

            System.out.println("#" + test_case);
            for(int i = 0; i < n; i++) {
            	for(int j =0; j <n; j++) {
                	System.out.print(snail[i][j] + " ");
                }
                System.out.println();
            }
		}
	}
}