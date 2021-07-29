import java.util.Scanner;
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
            List<Integer> records = new ArrayList<>();
            for(int i = 0; i < n; i++){
                int money = sc.nextInt();
                if(money == 0){
                    records.remove(records.size() - 1);
                } else {
                    records.add(money);
                }
            }

            int sum = 0;
            for(int record : records){
                sum += record;
            }
            System.out.println("#" + test_case + " " + sum);
		}
	}
}