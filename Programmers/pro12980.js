function solution(n)
{
    var ans = 0;

    while(n > 0) {
        if(n % 2 === 0) {
            n = parseInt(n / 2, 10);
        } else {
            n--;
            ans++;
        }
    }

    return ans;
}