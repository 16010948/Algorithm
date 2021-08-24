import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static class Edge implements Comparable<Edge>{
		int start, end, weight;

		public Edge(int start, int end, int weight) {
			super();
			this.start = start;
			this.end = end;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}

	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

		final int INFINITY = 11 * 20000;
		int[] minEdge = new int[V + 1];

		boolean[] visited = new boolean[V + 1];
		int start = Integer.parseInt(br.readLine());
		List<Edge>[] list = new ArrayList[V + 1];

		for(int i = 1; i <= V; i++) {
			list[i] = new ArrayList<>();
		}

		for(int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());

			list[u].add(new Edge(u, v, w));
		}

		Arrays.fill(minEdge, INFINITY);

		minEdge[start] = 0;
		for(int i = 1; i <= V; i++) {
			int min = INFINITY;
			int minVertex = -1;

			for(int j = 1; j <= V; j++) {
				if(!visited[j] && min > minEdge[j]) {
					min = minEdge[j];
					minVertex = j;
				}
			}

			if(minVertex >= 0) {
				visited[minVertex] = true;

				for(Edge edge : list[minVertex]) {
					if(!visited[edge.end] && minEdge[edge.end] > min + edge.weight) {
						minEdge[edge.end] = min + edge.weight;
					}
				}
			}
		}

		for(int i = 1; i <= V; i++) {
			if(minEdge[i] == INFINITY)
				System.out.println("INF");
			else
				System.out.println(minEdge[i]);
		}
	}
}
