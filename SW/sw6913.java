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
            int m = sc.nextInt();
            int[] scores = new int[n];
            int maxScore = 0;
            for(int i = 0; i < n; i++){
                int score = 0;
                for(int j = 0; j < m; j++){
                	if(sc.nextInt() == 1){
                    	score++;
                    }
                    scores[i] = score;
                }
                maxScore = Math.max(maxScore, score);
            }

            int count = 0;
            for(int score : scores){
                if(score == maxScore) {
                    count++;
                }
            }

            System.out.println("#" + test_case + " " + count + " " + maxScore);
		}
	}
}