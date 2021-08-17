import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            int N = sc.nextInt();
            int[] result = new int[3];
            int startX = Math.min(x1, x2);
            int endX = Math.max(x1, x2);
            int startY = Math.min(y1, y2);
            int endY = Math.max(y1, y2);
            for(int i = 0; i < N; i++) {
            	int x = sc.nextInt();
                int y = sc.nextInt();

                if(startX < x && x < endX  && startY < y && y < endY) {
                	result[0]++;
                } else if((x == x1 || x == x2) && startY <= y && y <= endY) {
                	result[1]++;
                } else if((y == y1 || y == y2) && startX <= x && x <= endX) {
                	result[1]++;
                } else{
                	result[2]++;
                }
            }

            System.out.println("#" + test_case + " " + result[0] + " " + result[1] + " " + result[2]);
        }
     }
}