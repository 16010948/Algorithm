function solution(k, m, score) {
    var answer = 0;

    const sorted = score.sort((a, b) => b - a);
    const length = sorted.length;
    for(let i = m - 1; i < length; i += m) {
        answer += sorted[i] * m;
    }

    return answer;
}