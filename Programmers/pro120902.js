function solution(my_string) {
    const stack = [];

    let sign = 1;
    for(let element of my_string.split(' ')) {
        if(element === '+') {
            sign = 1;
        } else if(element === '-'){
            sign = -1;
        } else {
            stack.push(sign * element);
        }
    }

    return stack.reduce((a, b) => a + b, 0);
}