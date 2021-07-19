import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{

			int n = sc.nextInt();
            String answer = sc.next();
            String mine = sc.next();
            int score = 0;
            for(int i = 0; i < n; i++){
                if(answer.charAt(i) == mine.charAt(i)){
                	score++;
                }
            }
            System.out.println("#" + test_case + " " + score);

		}
	}
}