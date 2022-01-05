function solution(numbers) {
    var answer = 45 - numbers.reduce((number, sum) => number + sum, 0);

    return answer;
}