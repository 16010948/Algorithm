import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Solution
{
    static int N;
    static List<Integer> primes = new ArrayList<>();
    static int size;
    static int answer;

	static void getPrime() {
        boolean[] isNotPrime = new boolean[999 + 1];
    	for(int i = 2; i <= Math.sqrt(999); i++) {
            if(!isNotPrime[i]) {
                for(int j = i * 2; j <= 999; j += i) {
                    isNotPrime[j] = true;
                }
            }
        }

        for(int i = 2; i <= 999; i++) {
        	if(!isNotPrime[i]) primes.add(i);
        }
    }

    private static void makeSum(int start, int count, int sum) {
        if(sum > N) return;
    	if(count == 3) {
        	if(sum == N) answer++;
            return;
        }

        for(int i = start; i < size; i++) {
        	makeSum(i, count + 1, sum + primes.get(i));
        }
    }

    public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		getPrime();
        size = primes.size();
        for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
            answer = 0;
            makeSum(0, 0, 0);

            System.out.println("#" + test_case + " " + answer);
		}
	}
}