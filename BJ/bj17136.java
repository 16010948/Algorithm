import java.util.Scanner;

public class Main {
	static int[] color;
	static int[][] paper;
	static int answer;
	static final int OUTER_SIZE = 10;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		color = new int[]{0, 5, 5, 5, 5, 5};
		paper = new int[10][10];
		for(int i = 0; i < OUTER_SIZE; i++) {
			for(int j = 0; j < OUTER_SIZE; j++) {
				paper[i][j] = sc.nextInt();
			}
		}

		answer = Integer.MAX_VALUE;
		dfs(0, 0, 0);
		System.out.println(answer);
	}

	private static void dfs(int r, int c, int count) {
		int[] position = findOne(r, c);
		if(position[0] == -1 || position[1] == -1) {
			answer = Math.min(answer, count);
			return;
		}

		for(int k = 5; k > 0; k--) {
			if(isAvailable(position[0], position[1], k)) {
				attach(position[0], position[1], k);
				color[k]--;
				dfs(position[0], position[1] + k, count + 1);
				detach(position[0], position[1], k);
				color[k]++;
			}
		}
	}

	private static int[] findOne(int r, int c) {
		int startY = c;
		for(int i = r; i < OUTER_SIZE; i++) {
			for(int j = startY; j < OUTER_SIZE; j++) {
				if(paper[i][j] == 1) {
					return new int[] {i, j};
				}
			}
			startY = 0;
		}
		return new int[] {-1, -1};
	}

	private static boolean isAvailable(int r, int c, int size) {
		if(r + size > OUTER_SIZE || c + size > OUTER_SIZE || color[size] <= 0) return false;
		int area = 0;
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < size; j++) {
				if(paper[r + i][c + j] != 1) return false;
			}
		}
		return true;
	}

	private static void attach(int r, int c, int size) {
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < size; j++) {
				paper[r + i][c + j] = 0;
			}
		}
	}

	private static void detach(int r, int c, int size) {
		for(int i = 0; i < size; i++) {
			for(int j = 0; j < size; j++) {
				paper[r + i][c + j] = 1;
			}
		}
	}
}
