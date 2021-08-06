import java.util.Scanner;

class Solution
{
    static int sum(int n) {
    	return (n * (n + 1)) / 2;
    }

    static int[] getCoordinate(int dot) {
    	int mostLeft = 0;
        int[] coord = {1, 1};
        while(mostLeft < dot) {
        	mostLeft += coord[1]++;
        }
        mostLeft = mostLeft - --coord[1];
        coord[0] += dot - mostLeft - 1;
        coord[1] -= dot - mostLeft - 1;

        return coord;
    }

    static int getDotNum(int[] coord) {
        return sum(coord[0] - 1 + coord[1] - 1) + coord[0];
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int a = sc.nextInt();
            int b = sc.nextInt();

            int[] coordA = getCoordinate(a);
            int[] coordB = getCoordinate(b);
            int[] coordR = {coordA[0] +coordB[0], coordA[1] + coordB[1]};
            System.out.println("#" + test_case + " " + getDotNum(coordR));
		}
	}
}