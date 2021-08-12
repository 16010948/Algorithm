import java.util.Scanner;

class Main {
	static final int N = 9;
	static final int R = 7;
	static final int HEIGHT = 100;

	static void mergeSort(int[] array, int start, int end) {
		if(start >= end) {
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

	private static boolean np(int[] array) {
		int i = N - 1;
		while(i > 0 && array[i - 1] >= array[i]) --i;
		if(i == 0) return false;

		int j = N - 1;
		while(array[i - 1] >= array[j]) --j;
		swap(array, i - 1, j);

		int k = N - 1;
		while(i < k) {
			swap(array, i++, k--);
		}

		return true;
	}

	private static void swap(int[] array, int i, int j) {
		int tmp = array[i];
		array[i] = array[j];
		array[j] = tmp;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] height = new int[N];
		for(int i = 0; i < N; i++) {
			height[i] = sc.nextInt();
		}

		int[] p = new int[N];
		int cnt = 0;
		while(++cnt <= R) p[N - cnt] = 1;

		do {
			int total = 0;
			int[] select = new int[R];
			int j = 0;
			for(int i = 0; i < N; i++) {
				if(p[i] == 1) {
					total += height[i];
					select[j++] = height[i];
				}
			}

			if(total == HEIGHT) {
				mergeSort(select, 0, R - 1);
				for(int i = 0; i < R; i++) {
					System.out.println(select[i]);
				}
				break;
			}
		}while(np(p));
	}
}

