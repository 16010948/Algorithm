import java.util.Scanner;

class Main
{

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int n = sc.nextInt();
            int result = 1;
            for(int i = 1; i <= n; i++) {
                int v = sc.nextInt();
                char data = sc.next().charAt(0);
                // 정점이 리프노드가 아닌 경우
                if (v <= n / 2) {
                	int left = sc.nextInt();
                	// n이 홀수일 때는 마지막이 오른쪽 자식
                	// n이 짝수일 때는 마지막이 왼쪽 자식
                	if(v < n / 2 + (n % 2)) {
                		int right = sc.nextInt();
                	}
                	if(Character.isDigit(data)) {
                		// 리프노드가 아닐 때 숫자가 나오면 연산 불가능
                		result = 0;
                	}
                } else if(!Character.isDigit(data)){
                	// 리프노드일 때 숫자가 아니면 연산 불가능
                	result = 0;
                }
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}