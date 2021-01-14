# 여행을 떠날 수 있는 그룹 수의 최댓값
N = int(input())
fear = list(map(int, input().split()))
fear.sort()

result = 0  # 총 그룹의 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for x in fear:
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    print(x,count)
    if x <= count:  # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
        count = 0   # 현재 그룹에 포함된 모험가의 수 초기화
        result += 1 #총 그룹의 수 증가시키기

print(result)