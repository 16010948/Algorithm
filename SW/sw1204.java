import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{

			int t = sc.nextInt();
            int[] count = new int[101];
            int maxCount = 0;
            int maxScore = 0;
            int score;
            for(int i = 0; i < 1000; i++){
                score = sc.nextInt();
                count[score]++;
                if(count[score] > maxCount){
                    maxCount = count[score];
                    maxScore = score;
                } else if(count[score] == maxCount && score > maxScore) {
                    maxScore = score;
                }
            }
            System.out.println("#" + t + " " + maxScore);

		}
	}
}