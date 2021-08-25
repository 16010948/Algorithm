import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] mushroom = new int[10];

		int sum = 0;
		for(int i = 0; i < 10; i++) {
			mushroom[i] = sc.nextInt();

		}
		for(int i = 0; i < 10; i++) {
			if(sum < 100) {
				sum += mushroom[i];
				if(sum >= 100) {
					int gap1 = Math.abs(100 - sum);
					int gap2 = Math.abs(100 - (sum - mushroom[i]));
					if(gap1 > gap2) {
						sum -= mushroom[i];
					}
					break;
				}
			}
		}

		System.out.println(sum);
	}
}
