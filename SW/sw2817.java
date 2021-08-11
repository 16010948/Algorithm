import java.util.Scanner;

class Main
{
    static int N, K;
    static int[] array;
    static int answer;

    static private void powerSet(int idx, int sum) {
    	if(idx == N) {
            if(sum == K) answer++;
            return ;
        }

        // 현재 값을 포함시킬 때
        powerSet(idx + 1, sum + array[idx]);
        // 현재 값을 포함시키지 않을 때
        powerSet(idx + 1, sum);
    }

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

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
