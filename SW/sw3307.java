import java.util.Scanner;

class Solution
{
    static int bisecLeft(int[] array, int target, int n){
    	int mid;
        int start = 0;
        int end = n;

        while(start < end){
            mid = (start + end) / 2;
            if(target <= array[mid]){
            	end = mid;
            } else {
                start = mid + 1;
            }
        }
        return end;
    }

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            int[] array = new int[n];
            for(int i = 0; i < n; i++){
                array[i] = sc.nextInt();
            }

            int[] stack = new int[n];
            int index = -1;
            for(int i = 0; i < n; i++){
                if(index < 0 || stack[index] < array[i]){
                	stack[++index] = array[i];
                } else {
                	int position = bisecLeft(stack, array[i], index);
                    stack[position] = array[i];
                }
            }

            System.out.println("#" + test_case + " " + (index + 1));
		}
	}
}