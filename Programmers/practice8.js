function solution(phone_number) {
  var answer =
    "*".repeat(phone_number.length - 4) +
    phone_number.slice(phone_number.length - 4);
  return answer;
}

let phone_number = "01033334444";
// answer = "*******4444"
console.log(solution(phone_number));

phone_number = "027778888";
// answer = "******8888"
console.log(solution(phone_number));
