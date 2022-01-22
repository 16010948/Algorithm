sounds = input()
QUACK = "quack"

visited = [False] * len(sounds)
result = 0
for i in range(len(sounds)):
    idx = 0
    if not visited[i]:
        if sounds[i] != QUACK[idx]:
            result = -1
            break
        for j in range(i, len(sounds)):
            if sounds[j] == QUACK[idx] and not visited[j]:
                idx = (idx + 1) % 5
                visited[j] = True

        if idx == 0:
            result += 1
        else:
            result = -1
            break

print(result)