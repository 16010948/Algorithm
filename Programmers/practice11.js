function solution(n) {
    const primes = Array(n + 1).fill(true);
    var answer = n - 1;
    for(let i = 2; i <= Math.sqrt(n); i++){
        if(primes[i]){
            for(let j = i * i; j <= n; j += i){
                if(j % i === 0 && primes[j]){
                    primes[j] = false;
                    answer--;
                }
            }
        }
    }

    return answer;
}