import java.util.Scanner;
 
class Solution
{
    static int N;
    static int M;
    static int[] snack;
    static int answer;
     
    // 들고 갈 수 있는 과자의 최대 값 구함
    public static void getMaxSnack(int start, int total, int count) {
        // 2봉지 과자를 사고
        if(count == 2) {
            // 총 무게를 넘지 않으며
            // 최대 무게일 때
            if(total <= M && total > answer) {
                answer = total;
            }
            return;
        }
             
        for(int i = start; i < N; i++) {
            getMaxSnack(i + 1, total + snack[i], count + 1);
        }
    }
     
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
         
        for(int test_case = 1; test_case <= T; test_case++)
        {
            N = sc.nextInt();
            M = sc.nextInt();
            snack = new int[N];
            for(int i = 0; i < N; i++) {
                snack[i] = sc.nextInt();
            }
             
            answer = 0;
            getMaxSnack(0, 0, 0);
            System.out.println("#" + test_case + " " + (answer == 0 ? -1 : answer));
        }
    }
}