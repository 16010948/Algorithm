function solution(num) {
  var answer = num % 2 === 0 ? "Even" : "Odd";
  return answer;
}

let num = 3;
// answer = "Odd"
console.log(solution(num));

num = 4;
// answer = "Even"
console.log(solution(num));
