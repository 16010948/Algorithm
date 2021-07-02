const gcd = (a, b) => {
    if(b <= 0) return a;
    else return gcd(b, a % b);
}

function solution(arr) {
    var answer = 0;
    let a, b, c;

    while(arr.length > 1){
        a = arr.pop();
        b = arr.pop();
        c = gcd(a, b);
        arr.push((a * b) / c);
    }
    answer = arr[0];
    return answer;
}