import java.util.Scanner;

class Solution
{
    static int[] parents, rank;
    static int N;

    static void make() {
        parents = new int[N + 1];
        rank = new int[N + 1];
        for(int i = 1; i <= N; i++) {
        	parents[i] = i;
        }
    }

    static int find(int a) {
    	if(a == parents[a]) return a;
        return parents[a] = find(parents[a]);
    }

    static void union(int a, int b) {
    	int aRoot = find(a);
        int bRoot = find(b);

        if(aRoot != bRoot) {
        	if(rank[aRoot] > rank[bRoot]) {
            	parents[bRoot] = aRoot;
            } else {
                parents[aRoot] = bRoot;
                if(rank[aRoot] == rank[bRoot]) rank[bRoot]++;
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
            int M = sc.nextInt();

            make();

            System.out.print("#" + test_case + " ");
            for(int i = 0; i < M; i++) {
            	int command = sc.nextInt();
                int a = sc.nextInt();
                int b = sc.nextInt();

                switch(command) {
                    case 0:
                        union(a, b);
                        break;
                    case 1:
                        System.out.print((find(a) == find(b) ? "1" : "0"));
                        break;
                    default:
                        break;
                }
            }
            System.out.println();
		}
	}
}