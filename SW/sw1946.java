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
			int N = sc.nextInt();
            char[] C = new char[N];
            int[] K = new int[N];

            for(int i = 0; i < N; i++) {
            	C[i] = sc.next().charAt(0);
                K[i] = sc.nextInt();
            }

            System.out.println("#" + test_case);
            int count = 0;
            for(int i = 0; i < N; i++) {
            	for(int j = 0; j < K[i]; j++) {
                	System.out.print(C[i]);
                    count++;
                    if(count == 10){
                        System.out.println();
                    	count = 0;
                    }
                }
            }
            if(count != 10) System.out.println();
		}
	}
}