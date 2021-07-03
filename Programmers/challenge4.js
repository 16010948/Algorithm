const convertBinary = (n) => {
    let result = '';
    while(n > 0){
        if(n % 2 === 0) result = '0' + result;
        else result = '1' + result;
        n = parseInt(n / 2);
    }
    return '0' + result;
}

const convertDecimal = (n) => {
    let result = 0;
    let length = n.length;
    for(let i = length - 1; i >= 0; i--){
        if(n[i] === '1') result += Math.pow(2, length - i - 1);
    }
    return result;
}

const getNextNumber = (number) => {
    const binary = convertBinary(number).split("");
    const length = binary.length;
    for(let i = length - 1; i > 0; i--){
        if(binary[i - 1] + binary[i] === '01'){
            binary[i - 1] = '1';
            binary[i] = '0';
            break;
        }
    }

    return convertDecimal(binary);
}

function solution(numbers) {
    var answer = numbers.map(number =>
                             number % 2 === 0 ?
                             number + 1
                             : getNextNumber(number));

    return answer;
}