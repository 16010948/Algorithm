import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] paper = new int[100 + 1][100 + 1];

		int n = sc.nextInt();
		int area = 0;
		for(int k = 0; k < n; k++) {
			int x = sc.nextInt();
			int y = sc.nextInt();

			for(int i = 0; i < 10; i++) {
				for(int j = 0; j < 10; j++) {
					if(paper[x + i][y + j] == 0) {
						paper[x + i][y + j] = 1;
						area++;
					}
				}
			}
		}
		System.out.println(area);
	}
}
