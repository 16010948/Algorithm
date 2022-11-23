function solution(my_string) {
    var answer = my_string
                    .split(/\D+/)
                    .reduce((prev, cur) => prev + Number(cur), 0);
    
    return answer;
}