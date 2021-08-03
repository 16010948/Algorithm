import java.util.Scanner;

class Solution
{
    static void mergeSort(double[] array, int start, int end) {
    	if(start >= end) {
        	return;
        }
        int mid = (start + end) / 2;
        mergeSort(array, start, mid);
        mergeSort(array, mid + 1, end);

        int i1 = start;
        int i2 = mid + 1;
        int ia = start;
        double[] tmp = new double[end + 1];
        while(i1 <= mid || i2 <= end) {
        	if(i2 > end || (i1 <= mid && array[i1] > array[i2])) {
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
        final String[] grades = {
            "A+", "A0", "A-",
            "B+", "B0", "B-",
            "C+", "C0", "C-",
            "D0"
        };
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
            int K = sc.nextInt();

            double[] student = new double[N];
            double findScore = 0;
            for(int i = 0; i < N; i++) {
            	int mid = sc.nextInt();
                int fin = sc.nextInt();
                int assign = sc.nextInt();

                student[i] = mid *0.35 + fin * 0.45 + assign * 0.2;
                if(i + 1 == K) {
                	findScore = student[i];
                }
            }

            mergeSort(student, 0, N - 1);

            for(int i = 0; i < N; i++) {
            	if(student[i] == findScore) {
                    String grade = grades[i / (N / 10)];
                	System.out.println("#" + test_case + " " + grade);
                    break;
                }
            }

		}
	}
}