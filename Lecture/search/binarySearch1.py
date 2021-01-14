def cutting_rice_cake(rice_cake, target):
    cut = 0
    for r in rice_cake:
        if r > target:
            cut += r - target
    return cut

# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
N, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

result = 0
start = 0
end = max(rice_cake)
while start <= end:
    mid = (start + end) // 2
    cut = cutting_rice_cake(rice_cake, mid)
    # 떡의 양이 부족한 경우 더 많이 자르기
    if cut < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid
        start = mid + 1

print(result)