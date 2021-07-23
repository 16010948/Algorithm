import java.util.Scanner;

class Solution
{
    static int n;
    static int[] array;

    static void mergeSort(int start, int end) {
        if(start >= end) return;

        int mid = (start + end) / 2;
        mergeSort(start, mid);
        mergeSort(mid + 1, end);

        int i1 = start;
        int i2 = mid + 1;
        int ia = start;
        int[] tmp = new int[n];
        while(i1 <= mid || i2 <= end){
            if(i2 > end || (i1 <= mid && array[i1] < array[i2])){
                tmp[ia++] = array[i1++];
            } else {
                tmp[ia++] = array[i2++];
            }
        }

        for(int i = start; i <= end; i++){
            array[i] = tmp[i];
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			n = sc.nextInt();
           	array = new int[n];
            for (int i = 0; i < n; i++) {
                array[i] = sc.nextInt();
            }
            mergeSort(0, n - 1);

            System.out.print("#" + test_case + " ");
            for(int i = 0; i < n; i++) {
                System.out.print(array[i] + " ");
            }
            System.out.println();
		}

	}
}