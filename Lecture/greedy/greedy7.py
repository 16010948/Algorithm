# 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 모든 숫자를 더한한 값을 이어서 출력

data = input()
value = 0
result = []

for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우 더하기
    else:
        value += int(x)

# 알파벳 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우
if value != 0:
    # 가장 뒤에 삽입
    result.append(str(value))

# 리스트를 문자열로 변환하여 출력
print(''.join(result))