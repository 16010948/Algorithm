import java.util.Scanner;

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
            int[] route = new int[5001];
            for(int i =0; i < n; i++){
				int a = sc.nextInt();
            	int b = sc.nextInt();
                for(int j = a; j <= b; j++) {
                	route[j]++;
                }
            }

            StringBuilder sb = new StringBuilder();
            sb.append("#" + test_case + " ");
            int m = sc.nextInt();
            for(int i = 0; i < m; i++) {
            	sb.append(route[sc.nextInt()] + " ");
            }
            System.out.println(sb.toString());
		}
	}
}