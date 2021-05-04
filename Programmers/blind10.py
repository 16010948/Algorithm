def solution(msg):
    answer = []

    compression = {}
    for num in range(1, ord('Z') - ord('A') + 2):
        compression[chr(num + ord('A') - 1)] = num

    index = 27
    i = 0
    while i < len(msg):
        w = msg[i]
        i += 1
        c = msg[i] if i < len(msg) else ''
        while i < len(msg) and w + c in compression:
            w = w + c
            i += 1
            c = msg[i] if i < len(msg) else ''
        answer.append(compression[w])
        compression[w + c] = index
        index += 1
    return answer

msg = "KAKAO"
# answer = [11, 1, 27, 15]
print(solution(msg))

msg = "TOBEORNOTTOBEORTOBEORNOT"
# answer = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution(msg))

msg = "ABABABABABABABAB"
# answer = [1, 2, 27, 29, 28, 31, 30]
print(solution(msg))