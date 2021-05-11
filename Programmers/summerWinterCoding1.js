const isPrime = (num) => {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i == 0) return false;
  }
  return true;
};

function solution(nums) {
  var answer = 0;
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if (isPrime(nums[i] + nums[j] + nums[k])) answer++;
      }
    }
  }

  return answer;
}

let nums = [1, 2, 3, 4];
// answer = 1
console.log(solution(nums));

nums = [1, 2, 7, 6, 4];
// answer = 4
console.log(solution(nums));
