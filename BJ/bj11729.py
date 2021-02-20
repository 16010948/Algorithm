def hanoi(n, from_pos, to_pos, aux_pos, result):
    if n == 1:
        result.append((from_pos, to_pos))
        return result

    hanoi(n - 1, from_pos, aux_pos, to_pos, result)
    result.append((from_pos, to_pos))
    return hanoi(n - 1, aux_pos, to_pos, from_pos, result)

n = int(input())
result = hanoi(n, 1, 3, 2, [])

print(len(result))
for movement in result:
    print(movement[0], movement[1])