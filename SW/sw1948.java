import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        int[] DAYS = new int[] {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int m1 = sc.nextInt();
            int d1 = sc.nextInt();
            int m2 = sc.nextInt();
            int d2 = sc.nextInt();
            int gap = 0;

            for(int i = m1 + 1; i < m2; i++){
                gap += DAYS[i];
            }
            if(m1 != m2){
            	gap += DAYS[m1] - d1 + 1;
            }
            gap += d2;
            System.out.println("#" + test_case + " " + gap);

		}
	}
}