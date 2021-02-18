def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer

phone_number = "01033334444"
# answer = "*******4444"
print(solution(phone_number))

phone_number = "027778888"
# answer = "*****8888"
print(solution(phone_number))