const AMBIGUOUS = 4;
const INDICATORS = [
    ['R', 'T'],
    ['C', 'F'],
    ['J', 'M'],
    ['A', 'N']
];

const getScore = (type1, type2, score) => {
    if(score < AMBIGUOUS) {
        return [type1, AMBIGUOUS - score];
    } else {
        return [type2, score - AMBIGUOUS];
    }
};

function solution(survey, choices) {
    var answer = '';

    let scores = {
      R: 0, T: 0,
      C: 0, F: 0,
      J: 0, M: 0,
      A: 0, N: 0,
    };
    choices.map((choice, idx) => {
        const type1 = survey[idx][0];
        const type2 = survey[idx][1];

        const [type, score] = getScore(type1, type2, choice);
        scores[type] += score;
    });

    const result = INDICATORS.reduce((prev, indicator) => {
        if(scores[indicator[0]] < scores[indicator[1]]) {
            return prev + indicator[1];
        } else if(scores[indicator[0]] > scores[indicator[1]]) {
            return prev + indicator[0];
        } else {
            if(indicator[0] < indicator[1]) {
                return prev + indicator[0];
            } else {
                return prev + indicator[1];
            }
        }
    }, '');

    answer = result;

    return answer;
}