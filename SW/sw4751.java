import java.util.Scanner;


class Solution
{
	public static void main(String args[]) throws Exception
	{
        String[] template = new String[]{"..#.", ".#.#", "#.!.", ".#.#", "..#."};
        String[] lastTemplate = new String[]{".", ".", "#", ".", "."};
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
			String[] answer = new String[]{"", "", "", "", ""};
			String word = sc.next();
            for(int i = 0; i < word.length(); i++){
                for(int j = 0; j < template.length; j++){
                    answer[j] += template[j].replace("!", word.substring(i, i + 1));
                }
            }
            for(int i = 0; i < answer.length;i++){
                System.out.println(answer[i] + lastTemplate[i]);
            }
		}
	}
}