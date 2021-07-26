import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
            char[] head = new char[3];
            for(int i = 0; i < 3; i++) {
            	head[i] = Character.toUpperCase(sc.next().charAt(0));
            }

            System.out.print("#" + test_case + " ");
            for(char hc : head) {
            	System.out.print(hc);
            }
            System.out.println();
		}
	}
}