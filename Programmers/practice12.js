const mergeSort = (array) => {
    const n = array.length;
    if(n < 2){
        return array;
    }
    const mid = Math.floor(n / 2);
    const left = mergeSort(array.slice(0, mid));
    const right = mergeSort(array.slice(mid, n));
    return merge(left, right);
}

const merge = (left, right) => {
    const result = [];
    while(left.length && right.length){
        if(left[0] < right[0]){
            result.push(left.shift());
        } else {
            result.push(right.shift());
        }
    }

    while(left.length) result.push(left.shift());
    while(right.length) result.push(right.shift());
    return result;
}

function solution(arr, divisor) {
    var answer = arr.filter(num => num % divisor === 0);

    if(answer.length === 0){
        answer = [-1];
    } else {
        answer = mergeSort(answer);
    }

    return answer;
}