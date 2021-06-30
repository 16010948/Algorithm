const mergeSort = (array) => {
  if (array.length < 2) return array;
  const pivot = Math.floor(array.length / 2);
  const left = array.slice(0, pivot);
  const right = array.slice(pivot, array.length);
  return merge(mergeSort(left), mergeSort(right));
};

const merge = (left, right) => {
  const result = [];
  while (left.length && right.length) {
    if (left[0] <= right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }

  while (left.length) result.push(left.shift());
  while (right.length) result.push(right.shift());
  return result;
};

function solution(n, lost, reserve) {
  var answer = n;

  const _lost = lost.filter((l) => !reserve.includes(l));
  const _reserve = reserve.filter((r) => !lost.includes(r));

  mergeSort(_lost);
  const nonattendance = _lost.filter((l) => {
    const index = _reserve.findIndex((r) => r == l - 1 || r == l + 1);
    if (index >= 0) {
      _reserve.splice(index, 1);
      return false;
    } else {
      return true;
    }
  }).length;
  return answer - nonattendance;
}