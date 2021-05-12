function solution(a, b) {
  var answer = 1234567890;

  answer = a.reduce((total, item, i) => ((total += item * b[i]), total), 0);

  return answer;
}

let a = [1, 2, 3, 4];
let b = [-3, -1, 0, 2];
// answer = 3
console.log(solution(a, b));

a = [-1, 0, 1];
b = [1, 0, -1];
// answer = -2
console.log(solution(a, b));
