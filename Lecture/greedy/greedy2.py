# 문자열 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x' 혹은 '+' 연산자를 넣어
# 결과적으로 만들어 질 수 있는 가장 큰 수
data = input("입력: ")

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)