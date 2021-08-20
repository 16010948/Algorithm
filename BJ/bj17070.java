import java.util.Scanner;

public class Main {
	static int N;
	static int[][] house;
	static int[][] deltas = {{0, 1}, {1, 0}, {1, 1}};
	static int answer;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();

		house = new int[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				house[i][j] = sc.nextInt();
			}
		}

		answer = 0;
		house[0][0] = house[0][1] = 1;
		dfs(0, 1, 0);
		System.out.println(answer);
	}

	private static void dfs(int r, int c, int pipe) {
		if(r >= N - 1 && c >= N - 1) {
			if(r == N - 1 && c == N - 1) answer++;
			return;
		}

		switch(pipe) {
			case 0:
			case 1:
				if(setPipe(r, c, pipe)) {
					dfs(r + deltas[pipe][0], c + deltas[pipe][1], pipe);
					removePipe(r, c, pipe);
				}
				break;
			case 2:
				if(setPipe(r, c, 0)) {
					dfs(r + deltas[0][0], c + deltas[0][1], 0);
					removePipe(r, c, 0);
				}

				if(setPipe(r, c, 1)) {
					dfs(r + deltas[1][0], c + deltas[1][1], 1);
					removePipe(r, c, 1);
				}
				break;
			default:
				break;
		}

		boolean isAvailable = true;
		for(int i = 0; i < 3; i++) {
			if(!setPipe(r, c, i)) {
				isAvailable = false;
				break;
			}
		}
		if(isAvailable) dfs(r + deltas[2][0], c + deltas[2][1], 2);
		for(int i = 0; i < 3; i++) {
			removePipe(r, c, i);
		}

	}

	private static boolean setPipe(int r, int c, int pipe) {
		int nr = r + deltas[pipe][0];
		int nc = c + deltas[pipe][1];
		if(0 > nr || nr >= N || 0 > nc || nc >= N) return false;
		if(house[nr][nc] != 0) return false;

		house[nr][nc] = 2;
		return true;
	}

	private static boolean removePipe(int r, int c, int pipe) {
		int nr = r + deltas[pipe][0];
		int nc = c + deltas[pipe][1];
		if(0 > nr || nr >= N || 0 > nc || nc >= N) return false;
		if(house[nr][nc] != 2) return false;

		house[nr][nc] = 0;
		return true;
	}
}
