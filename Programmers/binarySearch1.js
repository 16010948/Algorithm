const binarySearch = (times, n, start, end) => {
    let mid, total;
    while(start < end) {
        mid = parseInt((start + end) / 2);
        total = times.reduce((s, time) => s + parseInt(mid / time), 0);
        if(total >= n) {
            end = mid;
        } else {
            start = mid + 1;
        }
    }
    return start;
};

function solution(n, times) {
    var answer = binarySearch(times, n, 1, Math.max.apply(null, times) * n);
    return answer;
}