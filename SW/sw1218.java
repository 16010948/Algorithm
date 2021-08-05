import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Stack {
    private List<Character> data;

    public Stack(){
        data = new ArrayList<>();
    }

    public void push(char ch) {
        data.add(ch);
    }

    public char pop() {
        char value = data.get(this.size() - 1);
        data.remove(this.size() - 1);

        return value;
    }

    public char peek() {
        return data.get(this.size() - 1);
    }

    public boolean isEmpty() {
        return this.size() == 0;
    }

    public int size() {
    	return data.size();
    }
}

class Solution
{
	public static void main(String args[]) throws Exception
	{
		String open = "([{<";
		Scanner sc = new Scanner(System.in);
		int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();
            String bracket = sc.next();

			Stack stack = new Stack();
            int result = 1;
			check: for(int i = 0; i < n; i++) {

               	if(open.contains(bracket.substring(i, i + 1))) {
                	stack.push(bracket.charAt(i));
                } else {
                    if(stack.size() == 0){
                        result = 0;
                    	break;
                    }
                    char openBracket = stack.pop();
                    switch(bracket.charAt(i)) {
                        case ')':
                        	if(openBracket != '('){
                            	result = 0;
                                break check;
                            }
                            break;
                        case ']':
                        	if(openBracket != '['){
                            	result = 0;
                                break check;
                            }
                            break;
                        case '}':
                        	if(openBracket != '{'){
                            	result = 0;
                                break check;
                            }
                            break;
                        case '>':
                        	if(openBracket != '<'){
                            	result = 0;
                                break check;
                            }
                            break;
                        default:
                            result = 0;
                            break check;
                    }
                }
            }
            if(stack.size() > 0) {
            	result = 0;
            }

            System.out.println("#" + test_case + " " + result);
		}
	}
}