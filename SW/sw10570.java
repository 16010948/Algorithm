import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    static boolean isPalindrome(int n){
    	String s = Integer.toString(n);
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) != s.charAt(s.length() - i - 1)){
                return false;
            }
        }
        return true;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int a = sc.nextInt();
            int b = sc.nextInt();
            int answer = 0;
            for(int i = a; i <= b; i++){
                int sqrt = (int)Math.sqrt(i);

                if(sqrt * sqrt == i && isPalindrome(sqrt) && isPalindrome(i)){
                    answer++;
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}