import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			String date = sc.next();
            int first = Integer.parseInt(date.substring(0, 2));
            int second = Integer.parseInt(date.substring(2, 4));

            String result;
            if(0 < first && first <= 12 && 0 < second && second <= 12) {
            	result = "AMBIGUOUS";
            } else if(0 < first && first <= 12 && (second > 12 || second == 0)) {
                result = "MMYY";
            } else if((first > 12 || first == 0) && 0 < second && second <= 12) {
                result = "YYMM";
            } else {
                result = "NA";
            }

            System.out.println("#" + test_case + " " + result);
		}
	}
}