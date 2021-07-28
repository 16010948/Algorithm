import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int a = 0;
            int distance = 0;
            for(int i = 0; i < n; i++){
                int command = sc.nextInt();
                if(command == 1) {
                    a += sc.nextInt();
                } else if(command == 2) {
                    a -= sc.nextInt();
                    if(a < 0) {
                        a = 0;
                    }
                }
                distance += a;
            }
            System.out.println("#" + test_case + " " + distance);
		}
	}
}