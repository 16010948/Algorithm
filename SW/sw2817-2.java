import java.util.Scanner;

class Solution
{
    static int N, K;
    static int[] array;
    static int answer;

    private static void powerSet(int idx, int sum) {
    	if(idx == N) {
            if(sum == K) answer++;
        	return;
        }
        powerSet(idx + 1, sum + array[idx]);
        powerSet(idx + 1, sum);
    }

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
            K = sc.nextInt();

            array = new int[N];
            for(int i = 0; i < N; i++) {
            	array[i] = sc.nextInt();
            }

            answer = 0;
            powerSet(0, 0);
            System.out.println("#" + test_case + " " + answer);
		}
	}
}