import java.util.Scanner;

class Solution
{
    static int[] scores;

    static void mergeSort(int start, int end) {
    	if(start >= end) {
            return;
        }
        int mid = (start+ end) / 2;
        mergeSort(start, mid);
        mergeSort(mid + 1, end);

        int i1 = start;
        int i2 = mid + 1;
        int ia = start;
        int[] tmp = new int[end + 1];
        while(i1 <= mid || i2 <= end) {
            if(i2 > end || (i1 <= mid && scores[i1] > scores[i2])) {
                tmp[ia++] = scores[i1++];
            } else {
                tmp[ia++] = scores[i2++];
            }
        }

        for(int i = start; i <= end; i++) {
            scores[i] = tmp[i];
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{

			int n = sc.nextInt();
            int k = sc.nextInt();
            scores = new int[n];

            for(int i = 0; i < n; i++) {
                scores[i] = sc.nextInt();
            }
            mergeSort(0, n - 1);
            int sum = 0;
            for(int i = 0; i < k; i++) {
                sum += scores[i];
            }
            System.out.println("#" + test_case + " " + sum);
		}
	}
}