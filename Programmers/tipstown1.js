function solution(s) {
  var answer = 0;

  const stack = [];
  for (let c of s) {
    if (stack[stack.length - 1] === c) stack.pop();
    else stack.push(c);
  }
  answer = stack.length > 0 ? 0 : 1;

  return answer;
}

let s = "baabaa";
// answer = 1
console.log(solution(s));

s = "cdcd";
// answer = 0
console.log(solution(s));
