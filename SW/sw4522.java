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
			String word = sc.next();
            String result = "Exist";
            int n = word.length();
            for(int i = 0; i < n / 2; i++) {
            	if(word.charAt(i) == '?' || word.charAt(n - i - 1) == '?') continue;
                if(word.charAt(i) != word.charAt(n - i - 1)) {
                	result ="Not exist";
                    break;
                }
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}