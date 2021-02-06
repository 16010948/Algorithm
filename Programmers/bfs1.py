def compare(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    return count


def change_word(begin, target, words):
    visited = [False] * len(words)
    queue = [(begin, 0)]
    while queue:
        v = queue.pop(0)
        for i in range(len(words)):
            if visited[i]:
                continue
            count = compare(words[i], v[0])
            if count == len(words[i]) - 1:
                if words[i] == target:
                    return v[1] + 1
                elif not visited[i]:
                    queue.append((words[i], v[1] + 1))
                    visited[i] = True

    return 0


def solution(begin, target, words):
    answer = 0

    answer = change_word(begin, target, words)

    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# answer = 4
print(solution(begin, target, words))

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
# answer = 0
print(solution(begin, target, words))
