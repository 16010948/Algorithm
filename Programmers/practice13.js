function solution(a, b) {
    var answer = ((a + b) * (Math.abs(a - b) + 1)) / 2;
    return answer;
}