deltas = ((0, -1), (-1, 0), (0, 1), (1, 0))

def is_range(h, w):
    return h >= 0 and h < H and w >= 0 and w < W


def break_ball(h, w, block, remove):
    power = block[h][w] - 1
    block[h][w] = 0

    for delta in deltas:
        nh = h
        nw = w
        for i in range(power):
            nh += delta[0]
            nw += delta[1]
            if is_range(nh, nw) and block[nh][nw] != 0:
                remove = max(remove, break_ball(nh, nw, block, remove + 1))
    return remove

def merge_block(block):
    for w in range(W):
        stack = []
        for h in range(H):
            if block[h][w] != 0:
                stack.append(block[h][w])
            block[h][w] = 0

        index = H - 1
        while stack:
            block[index][w] = stack.pop()
            index -= 1

def fall_ball(h, w, block):
    while h < H and block[h][w] == 0:
        h += 1
    if is_range(h, w):
        remove = break_ball(h, w, block, 1)
        merge_block(block)
        return remove
    return 0

def play(block, ball, count):
    global answer
    if ball == N:
        answer = max(answer, count)
        return
    for w in range(W):
        after_block = [[block[i][j] for j in range(W)] for i in range(H)]
        remove = fall_ball(0, w, after_block)
        play(after_block, ball + 1, count + remove)
        after_block = [[block[i][j] for j in range(W)] for i in range(H)]


T = int(input())

for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())

    block = []
    total = 0
    for i in range(H):
        block.append(list(map(int, input().split())))
        for j in range(W):
            if block[i][j] != 0:
                total += 1
    answer = 0
    play(block, 0, 0)
    print(total - answer)