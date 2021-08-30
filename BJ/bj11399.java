import java.util.Scanner;

public class Main {
	static int N;

	public static void mergeSort(int[] array) {
		int start = 0;
		int end = array.length - 1;
		mergeSort(array, start, end);
	}

	public static void mergeSort(int[] array, int start, int end) {
		if(start >= end) {
			return ;
		}
		int mid = (start + end) / 2;
		mergeSort(array, start, mid);
		mergeSort(array, mid + 1, end);

		int i1 = start;
		int i2 = mid + 1;
		int[] tmp = new int[end + 1];
		int ia = start;
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

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();

		int[] atm = new int[N];
		for(int i = 0; i < N; i++) {
			atm[i] = sc.nextInt();
		}

		mergeSort(atm);

		int answer = 0;
		int waiting = 0;
		for(int i = 0; i < N; i++) {
			waiting += atm[i];
			answer += waiting;
		}
		System.out.println(answer);
	}
}
