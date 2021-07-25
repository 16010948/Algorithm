import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			char[] input = sc.next().toCharArray();
            boolean[] isWrite = new boolean[10];
            for(char c : input) {
                int index = c - '0';
                isWrite[index] = !isWrite[index];
            }

            int answer = 0;
            for(boolean w : isWrite) {
                if(w){
                   answer++;
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}