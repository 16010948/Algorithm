import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		outer: for(int test_case = 1; test_case <= T; test_case++)
		{
			String cards = sc.next();
            boolean[] S = new boolean[13 + 1];
            boolean[] D = new boolean[13 + 1];
            boolean[] H = new boolean[13 + 1];
            boolean[] C = new boolean[13 + 1];
            int[] count = new int[4];
            for(int i = 0; i < cards.length(); i+= 3) {
                int cardNum = Integer.parseInt(cards.substring(i + 1, i + 2 + 1));
            	switch (cards.charAt(i)) {
                    case 'S':
                        if(S[cardNum]){
                            System.out.println("#" + test_case + " ERROR");
                            continue outer;
                        }
                        S[cardNum] = true;
                        count[0]++;
                        break;
                    case 'D':
                        if(D[cardNum]){
                            System.out.println("#" + test_case + " ERROR");
                            continue outer;
                        }
                        D[cardNum] = true;
                        count[1]++;
                        break;
                    case 'H':
                        if(H[cardNum]){
                            System.out.println("#" + test_case + " ERROR");
                            continue outer;
                        }
                        H[cardNum] = true;
                        count[2]++;
                        break;
                    case 'C':
                        if(C[cardNum]){
                            System.out.println("#" + test_case + " ERROR");
                            continue outer;
                        }
                        C[cardNum] = true;
                        count[3]++;
                        break;
                    default:
                        break;
                }
            }

            System.out.print("#" + test_case);
            for(int i = 0; i < 4; i++) {
            	System.out.print(" " + (13 - count[i]));
            }
            System.out.println();
		}
	}
}