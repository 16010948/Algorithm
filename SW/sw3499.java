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
            String[] card = new String[n];
          	for(int i = 0; i < n; i++) {
                card[i] = sc.next();
            }

            System.out.print("#" + test_case + " ");
            int half = n % 2 == 0 ? n / 2 : n / 2 + 1;
            for(int i = 0; i <half; i++) {
                System.out.print(card[i] + " ");
                if(half + i < n) {
                    System.out.print(card[half + i] + " " );
                }
            }
            System.out.println();
		}
	}
}