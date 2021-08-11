import java.util.Scanner;
class Solution
{
    static int carriage = 0;
    static int add(int a, int b) {
    	int sum = a + b + carriage;
        if(sum >= 10) {
            carriage = 1;
        } else {
        	carriage = 0;
        }
        return sum % 10;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			String a = sc.next();
            String b = sc.next();
            int aIndex = a.length() - 1;
            int bIndex = b.length() - 1;

            String result = "";
            while(aIndex >= 0 && bIndex >= 0) {
            	result = add(a.charAt(aIndex--) - '0', b.charAt(bIndex--) - '0') + result;
            }

            for(int i = aIndex; i >= 0; i--) {
            	result = add(a.charAt(i) - '0', 0) + result;
            }
            for(int i = bIndex; i >= 0; i--) {
            	result = add(b.charAt(i) - '0', 0) + result;
            }

            if(carriage == 1) {
            	result = "1" + result;
            }
            System.out.println("#" + test_case + " " + result);
		}
	}
}