def solution(sticker):
    answer = 0
    n = len(sticker)

    dp1 = [0] * n
    for i in range(1, n):
        if i == 1:
            dp1[i] = sticker[i]
        else:
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
        answer = max(answer, dp1[i])

    dp2 = [0] * n
    for i in range(n - 1):
        if i < 2:
            dp2[i] = sticker[0]
        else:
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
        answer = max(answer, dp2[i])

    if n == 1:
        answer = sticker[0]

    return answer