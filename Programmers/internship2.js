function solution(gems) {
  const length = gems.length;
  var answer = [1, length];
  const types = new Set(gems).size;
  const cart = new Map();
  let end = 0;
  for (let start = 0; start <= length - types; start++) {
    while (end < length && cart.size < types) {
      if (cart.has(gems[end])) cart.set(gems[end], cart.get(gems[end]) + 1);
      else cart.set(gems[end], 1);
      end++;
    }
    if (cart.size === types && answer[1] - answer[0] > end - start - 1)
      answer = [start + 1, end];
    cart.set(gems[start], cart.get(gems[start]) - 1);
    if (cart.get(gems[start]) === 0) cart.delete(gems[start]);
  }

  return answer;
}

let gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"];
// answer = [3, 7]
console.log(solution(gems));

gems = ["AA", "AB", "AC", "AA", "AC"];
// answer = [1, 3]
console.log(solution(gems));

gems = ["XYZ", "XYZ", "XYZ"];
// answer = [1, 1]
console.log(solution(gems));

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"];
// answer = [1, 5]
console.log(solution(gems));
