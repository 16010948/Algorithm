import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] paper = new int[1001][1001];

		int n = sc.nextInt();
		int[][] coordinate = new int[n][4];
		for(int k = 0; k < n; k++) {
			coordinate[k] = new int[] {sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt()};

			for(int i = 0; i < coordinate[k][3]; i++) {
				for(int j = 0; j < coordinate[k][2]; j++) {
					paper[coordinate[k][1] + i][coordinate[k][0] + j] = k + 1;
				}
			}
		}

		for(int k = 0; k < n; k++) {
			int count = 0;
			for(int i = 0; i < coordinate[k][3]; i++) {
				for(int j = 0; j < coordinate[k][2]; j++) {
					if(paper[coordinate[k][1] + i][coordinate[k][0] + j] == k + 1)
						count++;
				}
			}
			System.out.println(count);
		}
	}
}
