function solution(board, moves) {
  var answer = 0;

  const n = board.length;
  const stack = [];
  moves.map((move) => {
    for (let i = 0; i < n; i++) {
      if (board[i][move - 1] !== 0) {
        if (board[i][move - 1] === stack[stack.length - 1]) {
          stack.pop();
          answer += 2;
        } else stack.push(board[i][move - 1]);
        board[i][move - 1] = 0;
        break;
      }
    }
  });

  return answer;
}

let board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];
let moves = [1, 5, 3, 5, 1, 2, 1, 4];
// answer = 4
console.log(solution(board, moves));
