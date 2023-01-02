function solution(k, tangerine) {
    var answer = 0;

    const result = tangerine.reduce((prev, t) => {
        prev[t] = prev[t] + 1 || 1;
        return prev;
    }, {});

    const sorted = Object.values(result).sort((a, b) => b - a);
    for(let count of sorted) {
        if(k > 0) {
            k -= count;
            answer++;
        } else {
            break;
        }
    }

    return answer;
}