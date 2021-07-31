import java.util.Scanner;

class Solution
{
    static int pow(int r , int n){
        int base = 1;
        while(n > 0){
            if(n % 2 == 1){
                base *= r;
            }
            r *= r;
            n /= 2;
        }
        return base;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int len = pow(2, n) - 1;
            int[] tree = new int[len];

            for(int i = 0; i < len; i++) {
                tree[i] = sc.nextInt();
            }
            System.out.print("#" + test_case + " " );

            int index = len;
           for(int i = 0; i < n; i++) {
               index -= pow(2, n - i - 1);
               for(int j = 0; j < pow(2, i); j++) {
                   System.out.print(tree[index + j * pow(2, n - i)] + " ");
               }
               System.out.println();
           }

		}
	}
}