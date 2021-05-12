function solution(participant, completion) {
  var answer = "";

  const result = participant.reduce(
    (r, p) => ((r[p] = r[p] ? r[p] + 1 : 1), r),
    {}
  );
  completion.map((c) => result[c]--);

  for (let key in result) {
    if (result[key] > 0) {
      answer = key;
      break;
    }
  }

  return answer;
}

let participant = ["leo", "kiki", "eden"];
let completion = ["eden", "kiki"];
// answer = "leo"
console.log(solution(participant, completion));

participant = ["marina", "josipa", "nikola", "vinko", "filipa"];
completion = ["josipa", "filipa", "marina", "nikola"];
// answer = "vinko"
console.log(solution(participant, completion));

participant = ["mislav", "stanko", "mislav", "ana"];
completion = ["stanko", "ana", "mislav"];
// answer = "mislav"
console.log(solution(participant, completion));
