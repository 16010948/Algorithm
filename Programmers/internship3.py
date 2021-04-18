LEFT_NUMS = (1, 4, 7, 10)
RIGHT_NUMS = (3, 6, 9, 12)


def solution(numbers, hand):
    answer = ''

    left = 10
    right = 12
    for number in numbers:
        if number in LEFT_NUMS:
            answer += 'L'
            left = number
        elif number in RIGHT_NUMS:
            answer += 'R'
            right = number
        else:
            if number == 0:
                number = 11
            l_distance = (abs(number - left) + 1) // 3
            r_distance = (abs(right - number) + 1) // 3
            if left in LEFT_NUMS:
                l_distance += 1

            if right in RIGHT_NUMS:
                r_distance += 1

            if l_distance < r_distance:
                answer += 'L'
                left = number
            elif l_distance > r_distance:
                answer += 'R'
                right = number
            elif hand == 'left':
                answer += 'L'
                left = number
            else:
                answer += 'R'
                right = number

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
# answer = "LRLLLRLLRRL"
print(solution(numbers, hand))

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
# answer = "LRLLRRLLLRR"
print(solution(numbers, hand))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
# answer = "LLRLLRLLRL"
print(solution(numbers, hand))