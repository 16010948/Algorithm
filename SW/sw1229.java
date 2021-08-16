import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            List<Integer> password = new ArrayList<>();
            for(int i = 0; i < n; i++) {
            	password.add(sc.nextInt());
            }

            int m = sc.nextInt();
            for(int i = 0; i < m; i++) {
            	char command = sc.next().charAt(0);
                int start = sc.nextInt();
                int count = sc.nextInt();
                switch(command){
                    case 'I':
                        for(int j =0; j < count; j++) {
                        	password.add(start + j, sc.nextInt());
                        }
                        break;
                    case 'D':
                        for(int j =0; j < count; j++) {
                            password.remove(start);
                        }
                        break;
                    default:
                        break;
                }
            }
			System.out.print("#" + test_case);
            for(int i = 0; i < 10; i++) {
            	System.out.print(" " + password.get(i));
            }
            System.out.println();
		}
	}
}