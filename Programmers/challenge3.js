function checkBracket(brackets) {
  const stack = [];
  let open;
  for (let bracket of brackets) {
    switch (bracket) {
      case "[":
      case "{":
      case "(":
        stack.push(bracket);
        break;
      case "]":
        if (stack.length > 0 && stack[stack.length - 1] === "[") {
          stack.pop();
          break;
        } else {
          return false;
        }
      case "}":
        if (stack.length > 0 && stack[stack.length - 1] === "{") {
          stack.pop();
          break;
        } else {
          return false;
        }
      case ")":
        if (stack.length > 0 && stack[stack.length - 1] === "(") {
          stack.pop();
          break;
        } else {
          return false;
        }
    }
  }
  return stack.length > 0 ? false : true;
}

function solution(s) {
  var answer = [...s]
    .map((bracket, i) => s.slice(i) + s.slice(0, i))
    .map((brackets) => checkBracket([...brackets]))
    .filter((result) => result).length;

  return answer;
}

let s = "[](){}";
// answer = 3
console.log(solution(s));

s = "}]()[{";
// answer = 2
console.log(solution(s));

s = "[)(]";
// answer = 0
console.log(solution(s));

s = "}}}";
// answer = 0
console.log(solution(s));
