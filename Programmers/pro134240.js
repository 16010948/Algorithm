function solution(food) {
    var answer = '';

    const order = food.map((f, idx) => {
        return idx
                .toString()
                .repeat(parseInt(f / 2, 10));
    });
    answer = order.join('') + '0' + order.reverse().join('');
    return answer;
}