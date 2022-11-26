function solution(a, b, n) {
    var answer = 0;

    while(n >= a) {
        answer += parseInt(n / a, 10) * b;
        n = (parseInt(n / a, 10) * b) + (n % a);
    }

    return answer;
}