const quickSort = (array, start, end) => {
  if (start >= end) return;

  const pivot = start;
  let left = start + 1;
  let right = end;
  while (left <= right) {
    while (left <= end && array[left] <= array[pivot]) left++;
    while (right > start && array[right] >= array[pivot]) right--;
    if (left > right) {
      let tmp = array[pivot];
      array[pivot] = array[right];
      array[right] = tmp;
    } else {
      let tmp = array[left];
      array[left] = array[right];
      array[right] = tmp;
    }
  }

  quickSort(array, start, right - 1);
  quickSort(array, right + 1, end);
};

const binarySearch = (array, target) => {
  let start = 0;
  let end = array.length - 1;

  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    if (array[mid] === target) return mid;
    else if (array[mid] < target) start = mid + 1;
    else end = mid - 1;
  }

  return -1;
};

function solution(lottos, win_nums) {
  var answer = [];
  const LOTTO = 6;

  quickSort(lottos, 0, LOTTO - 1);
  const blurry = lottos.filter((lotto) => lotto === 0).length;
  const correct = win_nums.filter(
    (num) => binarySearch(lottos, num) >= 0
  ).length;
  answer.push(Math.min(LOTTO - (blurry + correct) + 1, LOTTO));
  answer.push(Math.min(LOTTO - correct + 1, LOTTO));

  return answer;
}

let lottos = [44, 1, 0, 0, 31, 25];
let win_nums = [31, 10, 45, 1, 6, 19];
// answer = [3, 5]
console.log(solution(lottos, win_nums));

lottos = [0, 0, 0, 0, 0, 0];
win_nums = [38, 19, 20, 40, 15, 25];
// answer = [1, 6]
console.log(solution(lottos, win_nums));

lottos = [45, 4, 35, 20, 3, 9];
win_nums = [20, 9, 3, 45, 4, 35];
// answer = [1, 1]
console.log(solution(lottos, win_nums));
