import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	static int N;
	static int[][] safe;
	static boolean[][] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Set<Integer> heights = new HashSet<>();
		N = sc.nextInt();

		safe = new int[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				safe[i][j] = sc.nextInt();
				heights.add(safe[i][j]);
			}
		}

		int answer = 1;
		for(int height : heights) {
			int count = 0;
			visited = new boolean[N][N];
			for(int i = 0; i <N; i++) {
				for(int j = 0; j < N; j++) {
					if(!visited[i][j] && safe[i][j] > height) {
 						count++;
						dfs(i, j, height);
					}
				}
			}
			answer = Math.max(answer, count);
		}
		System.out.println(answer);
	}

	static int[][] deltas = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
	static void dfs(int r, int c, int height) {
		visited[r][c] = true;
		for(int[] delta : deltas) {
			int nr = r + delta[0];
			int nc = c + delta[1];

			if(nr < 0 || nr >= N || nc < 0 || nc >= N)
				continue;
			if(visited[nr][nc] || safe[nr][nc] <= height)
				continue;

			dfs(nr, nc, height);
		}
	}
}
