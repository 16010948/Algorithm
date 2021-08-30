import java.util.Scanner;

class Solution
{
    static String ONE_HOLE = "ADOPQR";

	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			String str1 = sc.next();
			String str2 = sc.next();

            String result = "SAME";
            if(str1.length() != str2.length()) {
            	result = "DIFF";
            } else {
                for(int i = 0; i < str1.length(); i++) {
                    String s1 = str1.substring(i, i + 1);
                    String s2 = str2.substring(i, i + 1);
                	if((s1.equals("B") && !s2.equals("B")) || (s2.equals("B") && !s1.equals("B"))) {
                    	result = "DIFF";
                        break;
                    } else if((ONE_HOLE.contains(s1) && !ONE_HOLE.contains(s2)) || (ONE_HOLE.contains(s2) && !ONE_HOLE.contains(s1))) {
                    	result = "DIFF";
                        break;
                    }
                }
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}