function solution(s) {
    var answer = [];

    const position = {};
    [...s].map((char, idx) => {
        answer.push(idx - position[char] || -1);
        position[char] = idx;
    });

    return answer;
}