import java.util.Scanner;

public class Main {
	static int R, C;
	static char[][] board;
	static int answer;
	static char[] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();

		board = new char[R][C];
		for(int i = 0; i < R; i++) {
			board[i] = sc.next().toCharArray();
		}

		visited = new char[R * C];
		answer = 0;
		move(0, 0, 0);
		System.out.println(answer);
	}

	static int[][] deltas = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
	private static void move(int r, int c, int count) {
		if(count == R * C) {
			return;
		}

		visited[count++] = board[r][c];
		answer = Math.max(answer, count);
		for(int[] delta : deltas) {
			int nr = r + delta[0];
			int nc = c + delta[1];
			if(nr >= 0 && nr < R && nc >= 0 && nc < C && isAvailable(board[nr][nc], count)) {
				move(nr, nc, count);
			}
		}
	}

	private static boolean isAvailable(char alpha, int count) {
		for(int i = 0; i < count; i++) {
			if(visited[i] == alpha) {
				return false;
			}
		}
		return true;
	}
}
