import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
        int SIZE = 10;

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int max = 0;
            int min = 10001;
            double sum = 0;
            for(int i = 0; i < SIZE; i++) {
            	int num = sc.nextInt();
                sum += num;
                if(num > max) {
                	max = num;
                }
                if(num < min) {
                	min = num;
                }
            }
            sum -= max + min;
            System.out.printf("#%d %.0f%n", test_case, sum / (SIZE - 2));
		}
	}
}