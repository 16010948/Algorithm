function solution(X, Y) {
    var answer = '';

    const cntX = Array.from({length: 10}, () => 0);
    const cntY = Array.from({length: 10}, () => 0);

    [...X].map((n) => cntX[Number(n)]++);
    [...Y].map((n) => cntY[Number(n)]++);

    for(let i = 9; i >= 0; i--) {
        while(cntX[i] > 0 && cntY[i] > 0) {
            cntX[i]--;
            cntY[i]--;
            answer += i.toString();
        }
    }

    answer = answer.replace(/^0+/, '0');
    if(!answer) {
        answer = "-1";
    }

    return answer;
}