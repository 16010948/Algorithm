import java.util.Scanner;

class Solution
{

    static boolean isWinning(String winning, String lotto) {
        for(int i = 0; i < 8; i++) {
            if(winning.charAt(i) =='*'){
                continue;
            }
            if(winning.charAt(i) != lotto.charAt(i)) {
                return false;
            }
        }
        return true;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int m = sc.nextInt();

            String[] winning = new String[n];
            int[] prize = new int[n];
            for(int i = 0; i < n; i++) {
            	winning[i] = sc.next();
                prize[i] = sc.nextInt();
            }

            String[] lotto = new String[m];
            for(int i = 0; i < m; i++) {
            	lotto[i] = sc.next();
            }

            int answer = 0;
            for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                    if(isWinning(winning[j], lotto[i])) {
                        answer += prize[j];
                        break;
                    }
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}