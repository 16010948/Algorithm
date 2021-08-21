import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int[] day = new int[n];
            for(int i = 0; i < n; i++) {
            	day[i] = sc.nextInt();
            }

            boolean[] visited = new boolean[n];
            int answer = 0;
            for(int i =1; i < n; i++) {
                int arrive = day[i];
                if(!visited[i]) {
                    answer++;
                    for(int j = i; j <n; j++) {
                        if(day[j] == arrive) {
							arrive += day[i] - 1;
                            visited[j] = true;
                        }
                    }
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}