def solution(relation):
    col_cnt = len(relation[0])
    answer = 0

    last = pow(2, col_cnt)
    bits = [i for i in range(1, last + 1)]
    for idx, cols in enumerate(bits):
        keys = set()
        for row in range(len(relation)):
            key = []
            for col in range(len(relation[0])):
                if cols & (1 << col) == 1 << col:
                    key.append(relation[row][col])
            keys.add(tuple(key))
        if len(keys) == len(relation):
            for i in range(idx + 1, last):
                if (bits[i] & cols) == cols:
                    bits[i] = bits[i] & ~cols
            answer += 1

    return answer