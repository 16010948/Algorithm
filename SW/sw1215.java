import java.util.Scanner;

class Solution
{
    static final int SIZE = 8;

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int answer = 0;

            String[] board = new String[SIZE];
            for(int i = 0; i < SIZE; i++){
            	board[i] = sc.next();
            }

            for(int i = 0; i < SIZE; i++){
                for(int k = 0; k <= SIZE - n; k++){
                    boolean isPalindrome = true;
                    for(int j = 0; j < n / 2; j++){
                        if(board[i].charAt(k + j) != board[i].charAt(k + (n - 1) - j)){
                            isPalindrome = false;
                            break;
                        }
                    }
                    if(isPalindrome){
                        answer++;
                    }

                    isPalindrome = true;
                    for(int j = 0; j < n / 2; j++){
                        if(board[k + j].charAt(i) != board[k + (n - 1) - j].charAt(i)){
                            isPalindrome = false;
                            break;
                        }
                    }
                    if(isPalindrome){
                        answer++;
                    }
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}