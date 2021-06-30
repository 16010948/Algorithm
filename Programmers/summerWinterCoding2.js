const gcd = (a, b) => {
  if (b <= 0) {
    return a;
  }
  return gcd(b, a % b);
};

function solution(w, h) {
  var answer = w * h - (w + h - gcd(w, h));
  return answer;
}
