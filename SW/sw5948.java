import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution
{
    static int[] nums;
    static Set<Integer> set;
    static public void combination(int n, int start, int sum) {
        if(n == 3) {
            set.add(sum);
        	return;
        }

        for(int i = start; i < 7; i++) {
        	combination(n + 1, i + 1, sum + nums[i]);
        }
    }

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            set = new HashSet<>();
            nums = new int[7];
			for(int i = 0; i < 7; i++) {
                nums[i] = sc.nextInt();
            }

            combination(0, 0, 0);
            List<Integer> sums = new ArrayList<>(set);
            Collections.sort(sums, Collections.reverseOrder());
            System.out.println("#" + test_case + " " + sums.get(5 - 1));
		}
	}
}