function solution(babbling) {
    const babblinglRegExp = new RegExp(/^(aya|ye|woo|ma)+$/);
    const duplicationRegExp = new RegExp(/(aya|ye|woo|ma)\1+/);

    var answer = babbling
                    .filter(b => !b.match(duplicationRegExp))
                    .filter(b => b.match(babblinglRegExp))
                    .length;

    return answer;
}