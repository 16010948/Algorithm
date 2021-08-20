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
				if(isAvailable(r, c, pipe)) {
					dfs(r + deltas[pipe][0], c + deltas[pipe][1], pipe);
				}
				break;
			case 2:
				if(isAvailable(r, c, 0)) {
					dfs(r + deltas[0][0], c + deltas[0][1], 0);
				}

				if(isAvailable(r, c, 1)) {
					dfs(r + deltas[1][0], c + deltas[1][1], 1);
				}
				break;
			default:
				break;
		}

		for(int i = 0; i < 3; i++) {
			if(!isAvailable(r, c, i)) {
				return;
			}
		}
		dfs(r + deltas[2][0], c + deltas[2][1], 2);

	}

	private static boolean isAvailable(int r, int c, int pipe) {
		int nr = r + deltas[pipe][0];
		int nc = c + deltas[pipe][1];
		if(0 > nr || nr >= N || 0 > nc || nc >= N) return false;
		if(house[nr][nc] != 0) return false;

		return true;
	}
}
