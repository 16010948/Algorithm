import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			String[] word = new String[5];
            int maxLength = 0;
            for(int i = 0; i < 5; i++) {
            	word[i] = sc.next();

                if(maxLength < word[i].length()) {
                	maxLength = word[i].length();
                }
            }

            System.out.print("#" + test_case + " ");
            for(int j = 0; j < maxLength; j++) {
               for(int i = 0; i <5; i++) {
               		if(j < word[i].length()){
                    	System.out.print(word[i].charAt(j));
                    }
               }
           }
           System.out.println();
		}
	}
}