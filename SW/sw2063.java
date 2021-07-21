import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();

        int[] count = new int[101];
        for(int i = 0; i < N; i++)
		{
			int score = sc.nextInt();
            count[score]++;
		}

        int countSum = 0;
        for(int i = 0; i <= 100; i++){
            countSum += count[i];
            if(countSum >= (N / 2) + 1) {
                System.out.println(i);
                break;
            }
        }
	}
}