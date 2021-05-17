function solution(nums) {
  var answer = Math.min(parseInt(nums.length / 2), [...new Set(nums)].length);
  return answer;
}

let nums = [3, 1, 2, 3];
// answer = 2
console.log(solution(nums));

nums = [3, 3, 3, 2, 2, 4];
// answer = 3
console.log(solution(nums));

nums = [3, 3, 3, 2, 2, 2];
// answer = 2
console.log(solution(nums));
