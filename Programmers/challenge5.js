function solution(left, right) {
    var answer = 0;

    for(let i = left; i <= right; i++){
        if(Math.pow(Math.floor(Math.sqrt(i)), 2) === i){
            answer -= i;
        } else {
            answer += i;
        }
    }

    return answer;
}