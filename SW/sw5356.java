SW Expert Academy모의 테스트
user photo 백지영_0614729
제출결과
제출횟수 1 / 99
제출결과 정보
제출회차	제출시간	결과
1차	11:13:48
Pass
5356. 의석이의 세로로 말해요
문제 내용
시간 : 100개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 2초 / Python의 경우 4초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.


아직 글을 모르는 의석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.

이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.

다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래에 의석이가 칠판에 붙여 만든 단어들의 예가 있다.


A A B C D D

a f z z

0 9 1 2 1

a 8 E W g 6

P 5 h 3 k x



만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.


심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.

세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.

이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.

위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.

그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.

위에서 의석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:



Aa0aPAf985Bz1EhCz2W3D1gkD6x



칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.



[입력]


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.


각 테스트 케이스는 총 다섯 줄로 이루어져 있다.

각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.


[출력]


각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.



입력
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx	//Test Case 갯수
//Test Case #1의 시작




//Test Case #2의 시작




sample_input.txt
출력
#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x	//TC #1의 정답

sample_output.txt
문제 풀이
Language
Java(java-1.8.0)

1
import java.util.Scanner;
2
​
3
class Solution
4
{
5
    public static void main(String args[]) throws Exception
6
    {
7
        Scanner sc = new Scanner(System.in);
8
        int T=sc.nextInt();
9

10
        for(int test_case = 1; test_case <= T; test_case++)
11
        {
12
            String[] word = new String[5];
13
            int maxLength = 0;
14
            for(int i = 0; i < 5; i++) {
15
                word[i] = sc.next();
16

17
                if(maxLength < word[i].length()) {
18
                    maxLength = word[i].length();
19
                }
20
            }
21

22
            System.out.print("#" + test_case + " ");
23
            for(int j = 0; j < maxLength; j++) {
24
               for(int i = 0; i <5; i++) {
25
                    if(j < word[i].length()){
26
                        System.out.print(word[i].charAt(j));
27
                    }
28
               }
29
           }
30
           System.out.println();
31
        }
32
    }
33
}
TEST
Input 을 입력하고 Run을 선택하면 Output 결과를 확인할 수 있습니다. Input 값을 넣지 않으면 기본 Input값이 적용되어 실행됩니다. Test는 채점을 하는 것이 아니며 정답 여부를 알려주지 않습니다.

Input
Input값을 입력해 주세요.
Output

