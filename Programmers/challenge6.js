const convertBinary = (n) => {
    let result = "";
    while(n > 0){
        result = (n % 2).toString() + result;
        n = Math.floor(n / 2);
    }
    return result;
}

function solution(s) {
    var answer = [0, 0];
    let count;
    while(s !== "1"){
        count = 0;
        s.split("").map(bit => bit === '0'? count++ : count);
        s = convertBinary(s.length - count);
        answer[0]++;
        answer[1] += count;
    }

    return answer;
}