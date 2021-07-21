import java.util.Scanner;

class Solution
{
    static int[] array;
    static int N;
    static void mergeSort(int start, int end) {
        if(start >= end){
            return ;
        }
    	int mid = (start + end) / 2;
        mergeSort(start, mid);
        mergeSort(mid + 1, end);

        int i1 = start;
        int i2 = mid + 1;
        int ia = start;
        int[] tmp = new int[N];

        while(i1 <= mid || i2 <= end) {
            if(i2 > end || (i1 <= mid && array[i1] < array[i2])){
            	tmp[ia++] = array[i1++];
            } else {
                tmp[ia++] = array[i2++];
            }
        }

        for(int i = start ; i <= end; i++){
            array[i] = tmp[i];
        }
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		N=sc.nextInt();

        array = new int[N];
        for(int i = 0; i < N; i++)
		{
			array[i] = sc.nextInt();
		}
        mergeSort(0, N - 1);
        System.out.println(array[N / 2]);
	}
}