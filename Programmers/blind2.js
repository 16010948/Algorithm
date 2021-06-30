const combine = (count, str) => {
  if (count <= 1) {
    return str;
  } else {
    return count + str;
  }
};

function solution(s) {
  var answer = 1001;
  for (let i = 0; i < s.length; i++) {
    let prev = "";
    let count = 1;
    let current = "";
    let result = "";
    for (let j = 0; j < s.length; j += i + 1) {
      current = s.substr(j, i + 1);
      if (prev === current) {
        count++;
      } else {
        result += combine(count, prev);
        prev = current;
        count = 1;
      }
    }
    result += combine(count, current);
    answer = Math.min(answer, result.length);
  }
  return answer;
}
