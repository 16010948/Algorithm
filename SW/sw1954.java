import java.util.Scanner;
class Solution
{
	public static void main(String args[]) throws Exception
	{
        int[][] deltas = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int[][] snail = new int[n][n];
            int y = 0;
            int x = -1;
            int index = 0;
            int count = 1;
            while(count <= n * n) {
                int ny = y + deltas[index][0];
                int nx = x + deltas[index][1];
                
                if(nx < 0 || nx >= n || ny < 0 || ny >=n || snail[ny][nx] != 0){
            
                    index = (++index) % 4;
                } else {
                    snail[ny][nx] = count++;
                    y = ny;
                    x = nx;
                }
            }
            
            System.out.println("#" + test_case);
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    System.out.print(snail[i][j] + " ");
                }
                System.out.println();
            }
		}
	}
}