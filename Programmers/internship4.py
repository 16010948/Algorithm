def solution(gems):
    answer = [0, len(gems)]
    types = len(set(gems))
    cur_types = {gems[0]: 1}
    end = 0
    for start in range(len(gems) - types + 1):
        while len(cur_types) < types and end < len(gems) - 1:
            end += 1
            if gems[end] in cur_types:
                cur_types[gems[end]] += 1
            else:
                cur_types[gems[end]] = 1

        if len(cur_types) == types and answer[1] - answer[0] > end - start:
            answer = [start + 1, end + 1]

        if cur_types[gems[start]] == 1:
            del (cur_types[gems[start]])
        else:
            cur_types[gems[start]] -= 1

    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# answer = [3, 7]
print(solution(gems))

gems = ["AA", "AB", "AC", "AA", "AC"]
# answer = [1, 3]
print(solution(gems))

gems = ["XYZ", "XYZ", "XYZ"]
# answer = [1, 1]
print(solution(gems))

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# answer = [1, 5]
print(solution(gems))