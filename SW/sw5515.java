import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{

			int month = sc.nextInt();
            int day = sc.nextInt();
            int weekday = 4;
            for(int i = 1; i < month; i++){
                switch(i) {
                    case 1:
                    case 3:
                    case 5:
                    case 7:
                    case 8:
                    case 10:
                    case 12:
                        weekday = (weekday + 3) % 7;
                        break;
                    case 2:
                        weekday = (weekday + 1) % 7;
                        break;
                    case 4:
                    case 6:
                    case 9:
                    case 11:
                        weekday = (weekday + 2) % 7;
                        break;
                }
            }
            weekday = (--weekday + (day % 7)) % 7;
            weekday = weekday < 0 ? 6 : weekday;
            System.out.println("#" + test_case + " " + weekday);
		}
	}
}