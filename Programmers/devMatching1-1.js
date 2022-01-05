const merge = (left, right) => {
    const result = [];

    while(left.length !== 0 && right.length !== 0) {
        left[0] <= right[0] ? result.push(left.shift()) : result.push(right.shift());
    }

    return [...result, ...left, ...right];
}

const mergeSort = (array) => {
    if(array.length <= 1) return array;

    const mid = Math.floor(array.length / 2);
    const left = array.slice(0, mid);
    const right = array.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
}

const binarySearch = (target, array) => {
    let start = 0;
    let end = array.length;
    while(start <= end) {
        const mid = Math.floor((start + end) / 2);
        if(array[mid] == target) return true;
        else if(array[mid] < target) start = mid + 1;
        else end = mid - 1;
    }
    return false;
}

function solution(lottos, win_nums) {
    const LOTTO = 6;
    var answer = [];

    const sorted = mergeSort(win_nums);
    const correct = lottos.filter(num => binarySearch(num, sorted)).length;
    const blank = lottos.filter(num => num === 0).length;

    answer.push(Math.min(LOTTO - (blank + correct) + 1, LOTTO));
    answer.push(Math.min(LOTTO - correct + 1, LOTTO));

    return answer;
}