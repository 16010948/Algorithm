function solution(new_id) {
  var answer = "";

  answer = new_id
    .toLowerCase()
    .replace(/[^\w-_.]/g, "")
    .replace(/\.+/g, ".")
    .replace(/^\.|\.$/g, "")
    .replace(/^$/, "a")
    .substr(0, 15)
    .replace(/\.$/, "");

  const n = answer.length;
  if (n <= 2) answer = answer + answer[n - 1].repeat(3 - n);

  return answer;
}

let new_id = "...!@BaT#*..y.abcdefghijklm";
// answer = "bat.y.abcdefghi"
console.log(solution(new_id));

new_id = "z-+.^.";
// answer = "z--"
console.log(solution(new_id));

new_id = "=.=";
// answer = "aaa"
console.log(solution(new_id));

new_id = "123_.def";
// answer = "123_.def"
console.log(solution(new_id));

new_id = "abcdefghijklmn.p";
// answer = "abcdefghijklmn"
console.log(solution(new_id));
