import java.util.Scanner;

class Solution
{
    static final int SIZE = 100;
    static int[] boxes;

    static void mergeSort(int start, int end) {
        if(start >= end) {
            return;
        }
        int mid = (start + end) / 2;
        mergeSort(start, mid);
        mergeSort(mid + 1, end);

        int i1 = start;
        int i2 = mid + 1;
        int ia = start;
        int[] tmp = new int[end + 1];
        while(i1 <= mid || i2 <= end){
        	if(i2 > end || (i1 <= mid && boxes[i1] <boxes[i2])) {
            	tmp[ia++] = boxes[i1++];
            } else {
                tmp[ia++] = boxes[i2++];
            }
        }

        for(int i = start; i <= end; i++){
            boxes[i] = tmp[i];
        }

    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = 10;

        for(int test_case = 1; test_case <= T; test_case++)
		{
            int n = sc.nextInt();
			boxes = new int[SIZE];
            for(int i = 0; i < SIZE; i++) {
                boxes[i] = sc.nextInt();
            }
            mergeSort(0, SIZE - 1);

            for(int i = 0; i < n; i++) {
                if(boxes[SIZE - 1] - boxes[0] <= 1){
                    break;
                }
                boxes[SIZE - 1]--;
                boxes[0]++;
                mergeSort(0, SIZE - 1);
            }
            System.out.println("#" + test_case + " " + (boxes[SIZE - 1] - boxes[0]));
		}
	}
}