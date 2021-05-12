function solution(absolutes, signs) {
  var answer = absolutes.reduce(
    (total, absolute, i) => (
      signs[i] ? (total += absolute) : (total -= absolute), total
    ),
    0
  );

  return answer;
}

let absolutes = [4, 7, 12];
let signs = [true, false, true];
// answer = 9
console.log(solution(absolutes, signs));

absolutes = [1, 2, 3];
signs = [false, false, true];
// answer = 0
console.log(solution(absolutes, signs));
