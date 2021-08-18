import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    static int N, B, E;
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            N = sc.nextInt();
            B = sc.nextInt();
            E = sc.nextInt();

            int answer = 0;
            for(int i = 0; i < N; i++) {
            	int sand = sc.nextInt();
                if(B + E >= sand) {
                    for(int time = B - E; time <= B + E; time++) {
                        if(time % sand == 0) {
                            answer++;
                            break;
                        }
                    }
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}