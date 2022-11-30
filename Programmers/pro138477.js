const findPosition = (target, array) => {
    let start = 0;
    let end = array.length - 1;
    while(start <= end) {
        const mid = parseInt((start + end) / 2, 10);
        if(array[mid] >= target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }

    return start;
};

function solution(k, score) {
    var answer = [];

    const fame = [];
    score.map((s) => {
        const position = findPosition(s, fame);

        if(position < k) {
            fame.splice(position, 0, s);

            if(fame.length > k) {
                fame.pop();
            }
        }

        answer.push(fame[fame.length - 1]);
    });

    return answer;
}