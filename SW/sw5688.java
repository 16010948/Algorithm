import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

        Map<Long, Long> cubic = new HashMap<>();
        for(long i = 1; i <= 1000000; i++) {
        	cubic.put(i * i * i, i);
        }

		for(int test_case = 1; test_case <= T; test_case++)
		{
			long n = sc.nextLong();
            Long answer = cubic.get(n);
            System.out.println("#" + test_case + " " + (answer == null? -1 : answer));
		}
	}
}