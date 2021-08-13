import java.util.Scanner;

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
    static int answer;

    static int getDistance(Point p1, Point p2) {
    	return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
    }

    static void permutation(int cnt, int total, Point cur) {
    	if(total > answer) return;

    	if(cnt == N + 1) {
            // 루트의 마지막을 도착점으로 지정
            total += getDistance(cur, dest);
            answer = Math.min(answer, total);
        	return;
        }
        for(int i = 0; i < N; i++) {
        	if(!isSelected[i]) {
        		int distance = getDistance(cur, customer[i]);
        		isSelected[i] = true;
                permutation(cnt + 1, total + distance, customer[i]);
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
            answer = Integer.MAX_VALUE;
            permutation(1, 0, start);

            System.out.println("#" + test_case + " " + answer);
		}
	}
}