import java.util.Scanner;

class Solution
{
    static int checkBit(String memory){
        char currentBit = '0';
        int count = 0;
        for(int i = 0; i < memory.length(); i++) {
            if(memory.charAt(i) != currentBit) {
                currentBit = currentBit == '0'? '1' : '0';
                count++;
            }
        }
        return count;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			String memory = sc.next();
            int count = checkBit(memory);
            System.out.println("#" + test_case + " " + count);
		}
	}
}