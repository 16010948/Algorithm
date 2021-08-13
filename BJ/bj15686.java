import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Main {

	static int N, M;
	static List<Integer[]> chicken;
	static List<Integer[]> house;
	static int C, H;
	static Integer[][] select;
	static int answer;

	private static void combination(int start, int count) {
		if(count <= M) {
			int total = 0;
			for(int i = 0; i < H; i++) {
				int min = 2 * N;
				for(int j = 0; j < count; j++) {
					min = Math.min(min, Math.abs((house.get(i)[0] - select[j][0])) + Math.abs((house.get(i)[1] - select[j][1])));
				}
				total += min;
			}
			answer = Math.min(answer, total);
		}

		if(count == M) return;

		for(int i = start; i < C; i++) {
			select[count] = chicken.get(i);
			combination(i + 1, count + 1);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();

		chicken = new ArrayList<>();
		house = new ArrayList<>();
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				int value = sc.nextInt();
				if(value == 1) {
					house.add(new Integer[]{i, j});
				} else if(value == 2) {
					chicken.add(new Integer[]{i, j});
				}
			}
		}
		H = house.size();
		C = chicken.size();

		answer = Integer.MAX_VALUE;
		select = new Integer[M][2];
		combination(0, 0);
		System.out.println(answer);
	}

}