import java.util.Scanner;
 
class Solution
{
    static int N, K;
    static int[] kcal;
    static int[] score;
    static int max;
     
    static void powerSet(int idx, int flag) {
        if(idx == N) {
            int totalKcal = 0;
            int totalScore =0;
            for(int i = 0; i < N; i++) {
                if((flag & (1 << i)) != 0){
                    totalKcal += kcal[i];
                    totalScore += score[i];
                }
            }
            // 총 칼로리가 제한 칼로리보다 낮고
            // 총 점수가 최대 값이 될 때
            if(totalKcal <= K && totalScore > max) {
                max = totalScore;
            }
            return;
        }
        powerSet(idx + 1, flag | (1 << idx));
        powerSet(idx + 1, flag);
    }
     
    public static void main(String args[]) throws Exception
    {
         
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
         
        for(int test_case = 1; test_case <= T; test_case++)
        {
            N = sc.nextInt();
            K = sc.nextInt();
            kcal = new int[N];
            score = new int[N];
            for(int i = 0; i < N; i++) {
                score[i] = sc.nextInt();
                kcal[i] = sc.nextInt();
            }
             
            max = 0;
            powerSet(0, 0);
            System.out.println("#" + test_case + " " + max);
        }
    }
}