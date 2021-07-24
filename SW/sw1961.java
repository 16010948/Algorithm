import java.util.Scanner;

class Solution
{
    static int N;
    static char[][] rotate(char[][] array) {
        char[][] result = new char[N][N];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++) {
                result[i][j] = array[N - j - 1][i];
            }
        }
        return result;
    }

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
            char[][] array = new char[N][N];

            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    array[i][j] = sc.next().charAt(0);
                }
            }

            String[][] answer = new String[N][3];
            for(int k = 0; k < 3; k++){
                array = rotate(array);
                for(int i = 0; i < N; i++){
                    answer[i][k] = String.valueOf(array[i]);
                }
            }

            System.out.println("#" + test_case);
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < 3; j++){
                    System.out.print(answer[i][j] + " ");
                }
                System.out.println();
            }
		}
	}
}