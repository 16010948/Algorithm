import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Solution
{
    static HashMap<Character,Integer> map = new HashMap<Character,Integer>(){{
        put('A', 0); put('B', 1); put('C', 2); put('D', 3); put('E', 4); put('F', 5); put('G', 6); put('H', 7);
        put('I', 8); put('J', 9); put('K', 10); put('L', 11); put('M', 12); put('N', 13); put('O', 14); put('P', 15);
        put('Q', 16); put('R', 17); put('S', 18); put('T', 19); put('U', 20); put('V', 21); put('W', 22); put('X', 23);
        put('Y', 24); put('Z', 25); put('a', 26); put('b', 27); put('c', 28); put('d', 29); put('e', 30); put('f', 31);
        put('g', 32); put('h', 33); put('i', 34); put('j', 35); put('k', 36); put('l', 37); put('m', 38); put('n', 39);
        put('o', 40); put('p', 41); put('q', 42); put('r', 43); put('s', 44); put('t', 45); put('u', 46); put('v', 47);
        put('w', 48); put('x', 49); put('y', 50); put('z', 51); put('0', 52); put('1', 53); put('2', 54); put('3', 55);
        put('4', 56); put('5', 57); put('6', 58); put('7', 59); put('8', 60); put('9', 61); put('+', 62); put('/', 63);
    }};

    public static String convertBinary(int n) {
        String result = "";
        while(n > 0) {
            result =  Integer.toString(n % 2) + result;
            n /= 2;
        }
        return result;
    }

    public static String adjustLength(String binary, int length) {
        int gap = length - binary.length();
        for(int i = 0; i < gap; i++){
            binary = "0" + binary;
        }
        return binary;
    }

    public static int convertDecimal(String binary) {
        int decimal = 0;
        int base = 1;
        for(int i = binary.length() - 1; i >= 0; i--){
            decimal += Integer.parseInt(binary.substring(i, i + 1)) * base;
            base *= 2;
        }
        return decimal;
    }

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
            String encoding = sc.next(), decoding = "", binary;
            int decimal;
            for(int i = 0; i < encoding.length(); i++) {
                binary = convertBinary(map.get(encoding.charAt(i)));
                decoding += adjustLength(binary, 6);
            }

            System.out.print("#" + test_case + " ");
            for(int i = 0; i < decoding.length(); i += 8){
                decimal = convertDecimal(decoding.substring(i, i + 8));
                System.out.print((char)decimal);
            }
            System.out.println();

		}
	}
}