const binarySearch = (array, target) => {
    let start = 0;
    let end = array.length - 1;

    while(start <= end) {
        const mid = Math.floor((start + end) / 2);
        if(array[mid] > target) {
            start = mid + 1;
        } else if(array[mid] < target) {
            end = mid - 1;
        } else {
            return mid;
        }
    }

    return -1;
};

const merge = (left, right) => {
    const result = [];

    while(left.length !== 0 && right.length !== 0) {
        left[0] > right[0] ? result.push(left.shift()) : result.push(right.shift());
    }

    return [...result, ...left, ...right];
}

const mergeSort = (array) => {
    if(array.length === 1) return array;

    const mid = Math.floor(array.length / 2);
    const left = array.slice(0, mid);
    const right = array.slice(mid);

    return merge(mergeSort(left), mergeSort(right));
}

function solution(emergency) {
    const sorted = mergeSort(emergency);
    var answer = emergency.map(e => binarySearch(sorted, e) + 1);

    return answer;
}