function solution(n) {
  const sqrt = Math.sqrt(n);
  var answer = n % sqrt === 0 ? Math.pow(sqrt + 1, 2) : -1;

  return answer;
}

let n = 121;
// answer = 144
console.log(solution(n));

n = 3;
// answer = -1
console.log(solution(n));
