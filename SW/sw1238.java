import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

class Solution
{
    static class Node {
   		int v;
        int depth;
        public Node(int v, int depth) {
        	this.v = v;
            this.depth = depth;
        }
    }

    static Map<Integer, List<Integer>> contact;
    static int answer;
    private static void bfs(int start) {
        boolean[] visited = new boolean[100 + 1];
        Queue<Node> queue = new LinkedList<>();
        int maxDepth = 0;

        queue.offer(new Node(start, 1));
        visited[start] = true;

        while(!queue.isEmpty()) {
        	Node cur = queue.poll();

            // 이전 보다 깊은 depth가 된다면 depth 갱신
            if(cur.depth > maxDepth) {
            	maxDepth = cur.depth;
                answer = cur.v;
            // depth가 현재 최대값인 경우 최대 정점 값으로 갱신
            } else if(maxDepth == cur.depth) {
            	answer = Math.max(answer, cur.v);
            }

            // 정점의 인접 노드들이 있으면 순회
            if(contact.containsKey(cur.v)){
                for(int adjacent : contact.get(cur.v)) {
                    if(!visited[adjacent]) {
                        // depth를 이전 보다 1 증가시킴
                        queue.add(new Node(adjacent, cur.depth + 1));
                        visited[adjacent] = true;
                    }
                }
            }
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int start = sc.nextInt();

            contact = new HashMap<>();
            for(int i = 0; i < n / 2; i++) {
            	int from = sc.nextInt();
                int to = sc.nextInt();

                // key가 없으면 추가
                if(!contact.containsKey(from)){
                	contact.put(from, new LinkedList<>());
                }
                // 인접 노드로 추가
                contact.get(from).add(to);
            }

            answer = 0;
            bfs(start);
            System.out.println("#" + test_case + " " + answer);
		}
	}
}