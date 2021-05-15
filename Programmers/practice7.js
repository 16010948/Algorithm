function solution(arr1, arr2) {
  var answer = arr1.map((row, i) => row.map((item, j) => item + arr2[i][j]));

  return answer;
}

let arr1 = [
  [1, 2],
  [2, 3],
];
let arr2 = [
  [3, 4],
  [5, 6],
];
// answer = [[4,6],[7,9]]
console.log(solution(arr1, arr2));

arr1 = [[1], [2]];
arr2 = [[3], [4]];
// answer = [[4],[6]]
console.log(solution(arr1, arr2));
