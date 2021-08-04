import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int n = sc.nextInt();
            char[][] farm = new char[n][n];
            for(int i = 0; i < n; i++) {
                farm[i] = sc.next().toCharArray();
            }

            int total = 0;
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < n; j++) {
                    // i 가 n / 2보다 작거나 같을 경우
                    // 마름모의 윗부분
                    if(n / 2 >= i) {
                        if(n / 2 - i <= j && j <= n / 2 + i){
                            total += farm[i][j] - '0';
                        }
                    } else {
                        // i 가 n / 2보다 클 경우
                        // 마름모의 아래 부분
                        if(n / 2 - (n - i - 1) <= j && j <= n / 2 + (n - i - 1)){
                            total += farm[i][j] - '0';
                        }
                    }
                }
            }
            System.out.println("#" + test_case + " " + total);
        }
    }
}