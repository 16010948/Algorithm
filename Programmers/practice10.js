function solution(s) {
    var answer = s.split(" ")
                 .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
                 .join(" ");
    return answer;
}