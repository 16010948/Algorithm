120861const DIRECTION = {
    up: [0, 1],
    down: [0, -1],
    left: [-1, 0],
    right: [1, 0],
};

const isRange = (position, direction, v, h) => {
    return Math.abs(position[0] + direction[0]) <= v
        && Math.abs(position[1] + direction[1]) <= h
};

function solution(keyinput, board) {
    var answer = [0, 0];

    const v = parseInt(board[0] / 2, 10);
    const h = parseInt(board[1] / 2, 10);
    keyinput.map((input) => {
        if(isRange(answer, DIRECTION[input], v, h)) {
            answer[0] += DIRECTION[input][0];
            answer[1] += DIRECTION[input][1];
        }
    });

    return answer;
}