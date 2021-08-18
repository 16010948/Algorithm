import java.util.Scanner;

public class Main {

	static int exp(int x, int n) {
		if(n == 0) return 1;
		if(n == 1) return x;

		int r = exp(x, n / 2);
		int res = r * r;
		if(n % 2 == 1) {
			res *= x;
		}
		return res;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();

		int value = 0;
		int rs = 0;
		int cs = 0;
		while(n-- > 0) {
			int half = exp(2, n);
			int diff = half * half;

			if(r < rs + half && cs + half <= c) {
				cs += half;
				value += diff;
			} else if(rs + half <= r && c < cs + half) {
				rs += half;
				value += diff * 2;
			} else if(rs + half <= r && cs + half <= c){
				rs += half;
				cs += half;
				value += diff * 3;
			}
		}

		System.out.println(value);
	}
}
