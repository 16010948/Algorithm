const dfs = (numbers, target, index, value) => {
  if (index === numbers.length) {
    if (target === value) {
      return 1;
    } else {
      return 0;
    }
  }
  return (
    dfs(numbers, target, index + 1, value + numbers[index]) +
    dfs(numbers, target, index + 1, value - numbers[index])
  );
};

function solution(numbers, target) {
  var answer = dfs(numbers, target, 0, 0);
  return answer;
}
