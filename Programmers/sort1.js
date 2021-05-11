function mergeSort(array) {
  const n = array.length;

  if (n <= 1) return;

  const mid = parseInt(n / 2);
  const g1 = array.slice(0, mid);
  const g2 = array.slice(mid, n);
  mergeSort(g1);
  mergeSort(g2);

  let i1 = 0;
  let i2 = 0;
  let ia = 0;
  while (i1 < g1.length && i2 < g2.length) {
    if (g1[i1] < g2[i2]) {
      array[ia] = g1[i1];
      i1++;
    } else {
      array[ia] = g2[i2];
      i2++;
    }
    ia++;
  }

  for (let i = i1; i < g1.length; i++) {
    array[ia++] = g1[i];
  }
  for (let i = i2; i < g2.length; i++) {
    array[ia++] = g2[i];
  }
}

function solution(array, commands) {
  var answer = [];

  for (let command of commands) {
    const sliceArray = array.slice(command[0] - 1, command[1]);
    mergeSort(sliceArray, 0, command[1] - command[0] + 1);
    answer.push(sliceArray[command[2] - 1]);
  }

  return answer;
}

let array = [1, 5, 2, 6, 3, 7, 4];
let commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];
// answer = [5, 6, 3]
console.log(solution(array, commands));
