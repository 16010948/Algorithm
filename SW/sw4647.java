import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    private static void mergeSort(int[] array, int start, int end) {
    	if(start >= end){
        	return;
        }
        int mid = (start + end) / 2;
        mergeSort(array, start, mid);
        mergeSort(array, mid + 1, end);

        int i1 = start;
        int i2 = mid + 1;
        int ia = start;
        int[] tmp = new int[end + 1];
        while(i1 <= mid || i2 <= end) {
        	if(i2 > end || (i1 <= mid && array[i1] < array[i2])) {
                tmp[ia++] = array[i1++];
            } else {
            	tmp[ia++] = array[i2++];
            }
        }

        for(int i = start; i <= end; i++) {
        	array[i] = tmp[i];
        }

    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			String word = sc.next() + " ";
            int n = sc.nextInt();
            int[] hyphen = new int[n];
            for(int i = 0; i < n; i++) {
            	hyphen[i] = sc.nextInt();
            }
            mergeSort(hyphen, 0, n - 1);

            int index = 0;
            System.out.print("#" + test_case + " ");
            for(int i = 0; i < word.length(); i++) {
            	while(index < n && hyphen[index] == i) {
                	System.out.print("-");
                    index++;
                }
                System.out.print(word.charAt(i));
            }
            System.out.println();
		}
	}
}