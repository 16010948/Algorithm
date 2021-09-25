def solution(scores):
    answer = ''

    n = len(scores)
    for i in range(n):
        max_index = -1
        max_score = 0

        min_index = -1
        min_score = 101

        sum_score = 0
        for j in range(n):
            if scores[j][i] > max_score:
                max_index = j
                max_score = scores[j][i]
            elif scores[j][i] == max_score:
                max_index = -1

            if scores[j][i] < min_score:
                min_index = j
                min_score = scores[j][i]
            elif scores[j][i] == min_score:
                min_index = -1

            sum_score += scores[j][i]

        student = n
        if max_index == i:
            sum_score -= max_score
            student -= 1
        elif min_index == i:
            sum_score -= min_score
            student -= 1
        avg = sum_score / student

        print(avg)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer