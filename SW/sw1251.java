import java.util.Arrays;
import java.util.Scanner;

public class Main
{
    static int N;
    static int[][] coordinates;
	static final int INFINITY = Integer.MAX_VALUE;

    static class Edge implements Comparable<Edge> {
		int vertex;
        double weight;

		public Edge(int vertex, double weight) {
			super();
			this.vertex = vertex;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return (int)(this.weight - o.weight);
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
            coordinates = new int[N][N];
            for(int j = 0; j < 2; j++) {
            	for(int i = 0; i < N; i++) {
                	coordinates[i][j] = sc.nextInt();
                }
            }

            double[] dist = new double[N];
            boolean[] visited = new boolean[N];
            Arrays.fill(dist, INFINITY);

            dist[0] = 0;
    		for(int i = 0; i < N; i++) {
    			double min = INFINITY;
    			int minVertex = -1;
    			for(int j = 0; j < N; j++) {
    				if(!visited[j] && min > dist[j]) {
    					min = dist[j];
    					minVertex = j;
    				}
    			}

    			visited[minVertex] = true;
    			dist[minVertex] = min;
    			for(int j = 0; j < N; j++) {
    				double tmp = Math.sqrt(Math.pow(Math.abs(coordinates[minVertex][0] - coordinates[j][0]), 2) + Math.pow(Math.abs(coordinates[minVertex][1] - coordinates[j][1]), 2));
    				if(!visited[j] && dist[j] > tmp) {
    					dist[j] = tmp;
    				}
    			}

    		}

            double tax = sc.nextDouble();
            double sum = 0;
            for(int i = 0; i < N; i++) {
            	sum += dist[i] * dist[i];
            }
            System.out.printf("#%d %.0f%n",test_case, sum * tax);
		}
	}
}
