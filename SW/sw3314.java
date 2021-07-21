import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int SIZE = 5;
        int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int sum = 0;
         	int score;
			for(int i = 0; i < SIZE; i++){
                score = sc.nextInt();
                if(score < 40){
                    score = 40;
                }
                sum += score;
            }
            System.out.println("#" + test_case +" " + (sum / SIZE));

		}
	}
}