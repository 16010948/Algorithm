function solution(progresses, speeds) {
  var answer = [];

  let deploy = 0;
  progresses.forEach((progress, i) => {
    let complete = Math.ceil((100 - progress) / speeds[i]);
    if (complete > deploy) {
      answer.push(1);
      deploy = complete;
    } else {
      answer[answer.length - 1]++;
    }
  });

  return answer;
}

let progresses = [93, 30, 55];
let speeds = [1, 30, 5];
// answer = [2, 1]
console.log(solution(progresses, speeds));

progresses = [95, 90, 99, 99, 80, 99];
speeds = [1, 1, 1, 1, 1, 1];
// answer = [1, 3, 2]
console.log(solution(progresses, speeds));
