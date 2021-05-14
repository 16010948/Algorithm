function solution(x, n) {
  var answer = [];

  for (let i = 0; i < n; i++) {
    answer.push(x + x * i);
  }

  return answer;
}

let x = 2;
let n = 5;
// answer = [2, 4, 6, 8, 10]
console.log(solution(x, n));

x = 4;
n = 3;
// answer = [4, 8, 12]
console.log(solution(x, n));

x = -4;
n = 2;
// answer = [-4, -8]
console.log(solution(x, n));
