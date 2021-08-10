import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int[][] pole = new int[n][];
            for(int i = 0; i < n; i++) {
            	pole[i] = new int[]{sc.nextInt(), sc.nextInt()};
            }

            int count = 0;
            for(int i = 0; i < n; i++) {
            	for(int j = i + 1; j < n; j++) {
                	if((pole[i][0] < pole[j][0] && pole[i][1] > pole[j][1]) || (pole[i][0] > pole[j][0] && pole[i][1] < pole[j][1])) {
                    	count++;
                    }
                }
            }
            System.out.println("#" + test_case + " " + count);
		}
	}
}