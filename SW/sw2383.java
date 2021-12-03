import java.util.Scanner;
import java.io.FileInputStream;
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

class Solution
{
    static final int STAIR_SIZE = 2;
    static final int CONCURRENT = 3;
    static int N;
    static Stair[] stair;
    static List<Coord> people;
    static int count;
    static int[] selected;
    static int answer;

    static class Coord {
    	int y;
        int x;

        public Coord(int y, int x) {
        	this.y = y;
            this.x = x;
        }
    }

    static class Stair extends Coord {
        int value;
        public Stair(int y, int x, int value) {
            super(y, x);
            this.value = value;
        }
    }

    public static int[] getDistance() {
        int[] distances = new int[count];
    	for(int i = 0; i < count; i++) {
            distances[i] = Math.abs(stair[selected[i]].y - people.get(i).y) + Math.abs(stair[selected[i]].x - people.get(i).x);
        }
        return distances;
    }

    static void init(Queue<Integer>[] queue) {
        for(int i = 0; i < STAIR_SIZE; i++) {
            queue[i] = new LinkedList<>();
        }
    }

    public static int downStair() {
        int[] distances = getDistance();

        int finished = 0;
        int time = 0;
        Queue<Integer>[] queue = new LinkedList[STAIR_SIZE];
        init(queue);

        while(true) {
            if(finished == count) break;

            for(int i = 0; i < STAIR_SIZE; i++) {
            	int size = queue[i].size();
                for(int j = 0; j < size; j++) {
                	int cur = queue[i].poll();
                    if(--cur == 0) {
                    	finished++;
                    } else {
                    	queue[i].offer(cur);
                    }
                }
            }

        	for(int i = 0; i < count; i++) {
                if(distances[i] > 0) {
                	distances[i]--;
                } else if(distances[i] == 0 && queue[selected[i]].size() < CONCURRENT) {
                    queue[selected[i]].add(stair[selected[i]].value);
                    distances[i]--;
                }
            }
            time++;
        }
        return time;
    }

    public static void selectStair(int idx) {
        if(idx == count) {
            answer = Math.min(answer, downStair());
            return;
        }
        selected[idx] = 0;
    	selectStair(idx + 1);

        selected[idx] = 1;
    	selectStair(idx + 1);
    }

    public static void run() {
        selected = new int[count];
    	selectStair(0);
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();

            stair = new Stair[STAIR_SIZE];
            people = new ArrayList<>();
            count = 0;
            int si = 0;
            for(int i = 0; i < N; i++) {
            	for(int j = 0; j < N; j++) {
                	int value = sc.nextInt();
                    if(value == 1) {
                    	people.add(new Coord(i, j));
                        count++;
                    } else if(value > 1) {
                    	stair[si++] = new Stair(i, j, value);
                    }
                }
            }

            answer = Integer.MAX_VALUE;
            run();
            System.out.println("#" + test_case + " " + answer);
		}
	}
}