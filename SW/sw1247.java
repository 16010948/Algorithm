import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Solution
{
    static class Point {
    	int x, y;
        Point(int x, int y) {
        	this.x = x;
            this.y = y;
        }
    }

    static int N;
    static Point start, dest;
    static Point[] customer;
    static boolean[] isSelected;
    static Point[] route;
    static int answer;

    static void permutation(int cnt) {
    	if(cnt == N + 1) {
            // 루트의 마지막을 도착점으로 지정
            route[cnt] = dest;

            int distance = 0;
            for(int i = 1; i <= N + 1; i++) {
                Point p1 = route[i - 1];
                Point p2 = route[i];
            	distance += Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
            }
            answer = Math.min(answer, distance);
        	return;
        }
        for(int i = 0; i < N; i++) {
        	if(!isSelected[i]) {
                route[cnt] = customer[i];
                isSelected[i] = true;
                permutation(cnt + 1);
                isSelected[i] = false;
            }
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();

            start = new Point(sc.nextInt(), sc.nextInt());
            dest = new Point(sc.nextInt(), sc.nextInt());
            customer = new Point[N];
            for(int i = 0; i < N; i++) {
            	customer[i] = new Point(sc.nextInt(), sc.nextInt());
            }

            isSelected = new boolean[N];
            route = new Point[N + 2];
            answer = Integer.MAX_VALUE;
            // 루트의 처음을 시작점으로 지정
            route[0] = start;
            permutation(1);

            System.out.println("#" + test_case + " " + answer);
		}
	}
}