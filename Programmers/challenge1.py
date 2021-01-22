def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = sorted(list(set(answer)))
    return answer

numbers = [2, 1, 3, 4, 1]
# answer = [2,3,4,5,6,7]
print(solution(numbers))

numbers = [5, 0, 2, 7]
# answer = [2,5,7,9,12]
print(solution(numbers))