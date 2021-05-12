function solution(n) {
  var answer = [];

  while (n > 0) {
    answer.push(n % 10);
    n = parseInt(n / 10);
  }

  return answer;
}

let n = 12345;
// answer = [5, 4, 3, 2, 1]
console.log(solution(n));
