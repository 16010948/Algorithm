function solution(arr) {
  var answer = arr.reduce((total, item) => total + item, 0) / arr.length;

  return answer;
}

let arr = [1, 2, 3, 4];
// answer = 2.5
console.log(solution(arr));

arr = [5, 5];
// answer = 5
console.log(solution(arr));
