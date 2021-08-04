import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Ladder1
{
	static int[][] ladder;
	static final int SIZE = 100;
	static List<Integer> cols;

	static int searchStart(int x) {
		int y = SIZE - 1;
		while (y >= 0) {
			if(x > 0 && ladder[y][x - 1] == 1) {
				for(int i = 1; i < cols.size(); i++) {
					if(cols.get(i) == x) {
						x = cols.get(i - 1);
						break;
					}
				}
			} else if(x < SIZE - 1 && ladder[y][x + 1] == 1) {
				for(int i = 0; i < cols.size() - 1; i++) {
					if(cols.get(i) == x) {
						x = cols.get(i + 1);
						break;
					}
				}
			}
		}

		return x;
	}

	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int T= 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int TC = sc.nextInt();

			ladder = new int[SIZE][SIZE];
			int destX = 0;
			cols = new ArrayList<>();
			for(int i = 0; i < SIZE; i++) {
				for(int j = 0; j < SIZE; j++) {
					ladder[i][j] = sc.nextInt();

					if(i == 0 && ladder[i][j]== 1) {
						cols.add(j);
					}
					if(ladder[i][j] == 2) {
						destX = j;
					}
				}
			}

			System.out.println("#" + test_case + " " + searchStart(destX));
		}
	}
}