import java.util.Scanner;

class Solution
{
    static int[][] ladder;
    static final int SIZE = 100;
    static boolean[][] visited;

    static boolean isArrive(int y, int x) {
        if(y >= SIZE || visited[y][x]){
        	return false;
        }

        if(ladder[y][x] == 2){
            return true;
        }

      visited[y][x] = true;
        if(x > 0 && !visited[y][x - 1] && ladder[y][x - 1] == 1){
            return isArrive(y, x - 1);
        } else if(x < SIZE - 1 && !visited[y][x + 1] && ladder[y][x + 1] == 1){
            return isArrive(y, x + 1);
        } else {
           return isArrive(y + 1, x);
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T= 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int TC = sc.nextInt();

            ladder = new int[SIZE][SIZE];
            for(int i = 0; i < SIZE; i++) {
            	for(int j = 0; j < SIZE; j++) {
                	ladder[i][j] = sc.nextInt();
                }
            }


            for(int x = 0; x < SIZE; x++) {

            	if(ladder[0][x] == 1){
                    visited = new boolean[SIZE][SIZE];
                    if(isArrive(0, x)){
                        System.out.println("#" + TC + " " + x);
                        break;
                    }
                }
            }

		}
	}
}