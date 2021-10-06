import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.io.FileInputStream;
 
class Solution
{
    static final int SQUARE = 4;
    static int HEX = 16;
    static int N, K;
    static int size;
   
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
         
        for(int test_case = 1; test_case <= T; test_case++)
        {
            N = sc.nextInt();
            K = sc.nextInt();
            size = N / SQUARE;
            String password = sc.next();
             
            List<Integer> numbers = getNumbers(password);
            mergeSort(numbers);
            System.out.println("#" + test_case + " " + numbers.get(K - 1));
        }
    }
     
    static void mergeSort(List<Integer> list) {
        int size = list.size();
        mergeSort(list, 0, size - 1);
    }
     
    static void mergeSort(List<Integer> list, int start, int end) {
        if(start >= end) return ;
        int mid = (start + end) / 2;
        mergeSort(list, start, mid);
        mergeSort(list, mid + 1, end);
         
        int i1 = start;
        int i2 = mid + 1;
        List<Integer> sorted = new ArrayList<>();
        while(i1 <= mid || i2 <= end) {
            if(i2 > end || (i1 <= mid && list.get(i1) > list.get(i2))) {
                sorted.add(list.get(i1++));
            } else {
                sorted.add(list.get(i2++));
            }
        }
         
        for(int i = start; i <= end; i++) {
            list.set(i, sorted.get(i - start));
        }
         
        return;
    }
     
    static List<Integer> getNumbers(String password) {
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < N; j += size) {
                String hex = password.substring(j, j + size);
                int decimal = parseDecimal(hex);
                set.add(decimal);
            }
            password = password.substring(1) + password.substring(0, 1);
        }
         
        List<Integer> numbers = new ArrayList<>(set);
        return numbers;
    }
     
    static int parseDecimal(String hex) {
        int decimal = 0;
        int base = 1;
        for(int i = size - 1; i >= 0; i--) {
            if(Character.isDigit(hex.charAt(i))) {
                decimal += (hex.charAt(i) - '0') * base;
            } else {
                decimal += (hex.charAt(i) - 'A' + 10) * base;
            }
            base *= 16;
        }
        return decimal;
    }
}