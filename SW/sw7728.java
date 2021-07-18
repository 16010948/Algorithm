import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            String num = sc.next();
			Set<Character> charSet = new HashSet<>();

            for(int i = 0; i < num.length(); i++){
                charSet.add(num.charAt(i));
            }

            System.out.println("#" + test_case + " " +charSet.size());
		}
	}
}