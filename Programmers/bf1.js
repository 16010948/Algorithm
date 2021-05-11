function solution(answers) {
  var answer = [];
  const student1 = [1, 2, 3, 4, 5];
  const student2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  const length1 = student1.length;
  const length2 = student2.length;
  const length3 = student3.length;

  const score1 = answers.filter((a, i) => a == student1[i % length1]).length;
  const score2 = answers.filter((a, i) => a == student2[i % length2]).length;
  const score3 = answers.filter((a, i) => a == student3[i % length3]).length;
  const maxScore = Math.max(score1, score2, score3);

  if (score1 == maxScore) answer.push(1);
  if (score2 == maxScore) answer.push(2);
  if (score3 == maxScore) answer.push(3);

  return answer;
}

let answers = [1, 2, 3, 4, 5];
// answer = [1]
console.log(solution(answers));

answers = [1, 3, 2, 4, 2];
// answer = [1, 2, 3]
console.log(solution(answers));
