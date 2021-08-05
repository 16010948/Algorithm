import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

class Solution
{
    static final int SIZE = 8;
    static final int CYCLE_SIZE = 5;
    static int[] DIFF = {1, 2, 3, 4, 5};

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=10;


        for(int test_case = 1; test_case <= T; test_case++)
		{
			int tc = sc.nextInt();
           	Queue<Integer> password = new LinkedList<>();
            int min = Integer.MAX_VALUE / 15;
            for(int i = 0; i < SIZE; i++) {
            	password.offer(sc.nextInt());
                // 배열 순회 5번에 각 자리 수가 15씩 작아짐
                int commonCircuit = password.peek() / 15;
                // 가장 적은 순회 횟수 검색
                if(commonCircuit < min) {
                	min = Math.max(commonCircuit - 1, 0);
                }
            }

            // 공통 순회만큼 값을 감소시킴
            for(int i = 0; i < SIZE; i++) {
            	password.offer(password.poll() - (15 * min));
            }

            // 공통 순회 이후 사이클 시작
            int index = 0;
            while(true) {
            	int value = Math.max(password.poll() - DIFF[index++ % 5], 0);
                password.offer(value);
                if(value == 0){
                	break;
                }
            }

            System.out.print("#" + tc + " ");
            for(int i = 0; i < SIZE; i++){
            	System.out.print(password.poll() + " ");
            }
            System.out.println();
		}
	}
}