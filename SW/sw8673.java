import java.util.Scanner;
import java.util.ArrayList;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			int k = sc.nextInt();
            ArrayList<Integer> list = new ArrayList<>();
            for(int i = 0; i < Math.pow(2, k); i++){
                list.add(sc.nextInt());
            }

            int answer = 0;
            while(list.size() > 1){
                int length = list.size();
                for(int i = 0; i < length / 2; i++){
                    int index;
                    if(list.get(i) < list.get(i + 1)) {
                        answer += list.get(i + 1) - list.get(i);
                    	list.remove(i);
                    } else {
                        answer += list.get(i) - list.get(i + 1);
                    	list.remove(i + 1);
                    }
                }
            }
            System.out.println("#" + test_case + " " + answer);
		}
	}
}