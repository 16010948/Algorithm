import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	static int N;
	static char[][] map;
	static List<Integer> sizes;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new char[N][N];

		for(int i = 0; i < N; i++) {
			map[i] = sc.next().toCharArray();
		}

		sizes = new ArrayList<>();
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(map[i][j] == '1') {
					sizes.add(0);
					dfs(i,j);
				}
			}
		}

		Collections.sort(sizes);
		System.out.println(sizes.size());
		for(int size: sizes) {
			System.out.println(size);
		}
	}

	static int[][] deltas = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
	static void dfs(int r, int c) {
		map[r][c] = '0';
		sizes.set(sizes.size()-1, sizes.get(sizes.size() - 1) + 1);
		for(int i = 0; i < 4; i++) {
			int nr = r + deltas[i][0];
			int nc = c + deltas[i][1];

			if(nr >= 0 && nr < N && nc >= 0 && nc < N && map[nr][nc] == '1') {
				dfs(nr, nc);
			}

		}
	}
}
