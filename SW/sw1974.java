import java.util.Scanner;

class Solution
{
    static int[][] sudoku;

    static boolean checkRow(int y) {
        boolean[] visited = new boolean[10];
        for(int x = 0; x < 9; x++) {
            if(visited[sudoku[y][x]]) {
                return false;
            }
            visited[sudoku[y][x]] = true;
        }
        return true;
    }

    static boolean checkCol(int x) {
        boolean[] visited = new boolean[10];
        for(int y = 0; y < 9; y++) {
            if(visited[sudoku[y][x]]) {
                return false;
            }
            visited[sudoku[y][x]] = true;
        }
        return true;
    }

    static boolean checkSquare(int y, int x) {
        boolean[] visited = new boolean[10];
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++){
                if(visited[sudoku[y + i][x + j]]) {
                    return false;
                }
                visited[sudoku[y + i][x + j]] = true;
            }
        }
        return true;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            sudoku = new int[9][9];
			for(int i = 0; i < 9; i++) {
            	for(int j = 0; j < 9; j++) {
                	sudoku[i][j] = sc.nextInt();
                }
            }

            int result = 1;
            for(int i = 0; i < 9; i++) {
                if(!checkRow(i) || !checkCol(i) || !checkSquare(3 * (i / 3) , 3 * (i % 3))) {
                    result = 0;
                    break;
                }
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}