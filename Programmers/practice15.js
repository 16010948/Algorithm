const getGcd = (a, b) => {
    if(b <= 0){
        return a;
    }
    return getGcd(b, a % b);
}

function solution(n, m) {
    const gcd = getGcd(n, m);
    const lcm = gcd * Math.floor(n / gcd) * Math.floor(m / gcd);
    var answer = [gcd, lcm];

    return answer;
}