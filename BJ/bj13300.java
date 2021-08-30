import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();

		int[] girls = new int[6 + 1];
		int[] boys = new int[6 + 1];
		int count = 0;
		for(int i = 0; i < N; i++) {
			int gender = sc.nextInt();
			int grade = sc.nextInt();

			if(gender == 0) {
				if(girls[grade] % K == 0) {
					count++;
				}
				girls[grade]++;
			} else {
				if(boys[grade] % K == 0) {
					count++;
				}
				boys[grade]++;
			}
		}

		System.out.println(count);
	}
}
