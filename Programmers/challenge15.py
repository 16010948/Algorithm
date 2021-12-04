def solution(arr):
    answer = [0, 0]

    def comp(r, c, n):
        start = arr[r][c]
        for i in range(r, r + n):
            for j in range(c, c + n):
                if start != arr[i][j]:
                    comp(r, c, n // 2)
                    comp(r + (n // 2), c, n // 2)
                    comp(r, c + (n // 2), n // 2)
                    comp(r + (n // 2), c + (n // 2), n // 2)
                    return
        answer[start] += 1

    comp(0, 0, len(arr))

    return answer