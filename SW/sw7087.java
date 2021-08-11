import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            Set<Character> title = new HashSet<>();

            for(int i = 0; i < n; i++) {
            	title.add(sc.next().charAt(0));
            }

            List<Character> titleArray = new ArrayList<>(title);
            titleArray.sort(null);
            int answer = 0;
            char alpha = 'A';
            for(char t : title) {
            	if(t != alpha){
                	break;
                }
                alpha++;
                answer++;
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}