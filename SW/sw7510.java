import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int n = sc.nextInt();

            int end = 1;
            int intervalSum = 1;
            int answer = 0;
            for(int start = 1; start <= (n / 2) + 1; start++) {
                while(end <= (n / 2) + 1 && intervalSum < n){
                    intervalSum += ++end;
                }
                if(intervalSum == n){
                    answer++;
                }
                intervalSum -= start;
            }
            if(n == 1){
                answer--;
            }
            System.out.println("#" + test_case + " " + (answer + 1));
		}
	}
}