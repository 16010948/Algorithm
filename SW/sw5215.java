import java.util.Scanner;

class Solution
{
    static int n;
    static int l;
    static int[] t;
    static int[] k;

    static int dfs(int kcal, int start, int score){
        if(kcal <= 0 || start >= n) {
            return score;
        }
        int max = score;
        for(int i = start; i < n; i++){
            if(kcal - k[i] >= 0){
                max = Math.max(max, dfs(kcal - k[i], i + 1, score + t[i]));
            }
        }
        return max;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			n = sc.nextInt();
            l = sc.nextInt();
            t = new int[n];
            k = new int[n];

            for(int i = 0; i < n; i++) {
                t[i] = sc.nextInt();
                k[i] = sc.nextInt();
            }

            System.out.println("#" + test_case + " " + dfs(l, 0, 0));
		}
	}
}