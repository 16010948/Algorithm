const convertTernary = (n) => {
    let result = '';
    while(n > 0){
        result = (n % 3).toString() + result;
        n = Math.floor(n / 3);
    }
    return result;
}

const convertDecimal = (n, base) => {
    let result = 0;
    let power = 1;
    for(let i = n.length - 1; i >= 0; i--){
        result += n[i] * power;
        power *= base;
    }
    return result;
}

function solution(n) {
    var answer = convertDecimal(convertTernary(n).split("").reverse(), 3);
    return answer;
}