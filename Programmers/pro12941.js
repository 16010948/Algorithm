function solution(A,B){
    var answer = 0;
    const sortedA = A.sort((a, b) => a - b);
    const sortedB = B.sort((a, b) => b - a);
    
    answer = sortedAc
                .map((e, idx) => e * sortedB[idx])
                .reduce((r, p) => r + p);

    return answer;
}