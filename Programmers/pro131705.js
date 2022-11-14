const N = 3;

const combination = (arr, idx, s, cnt) => {
    if(cnt > N) return 0;

    if(idx === arr.length) {
        if(cnt === N && s === 0) {
            return 1;
        }
        return 0;
    }

    let result = 0;
    result += combination(arr, idx + 1, s + arr[idx], cnt + 1);
    result += combination(arr, idx + 1, s, cnt);

    return result;
};

function solution(number) {
    var answer = combination(number, 0, 0, 0);

    return answer;
}