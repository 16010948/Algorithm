function solution(arr)
{
    var answer = arr.filter((num, index) => num !== arr[index + 1]);

    return answer;
}