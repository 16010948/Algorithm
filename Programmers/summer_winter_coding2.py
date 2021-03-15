def solution(n, words):
    answer = [0, 0]

    for i in range(len(words)):
        if i > 0 and (words[i] in words[:i] or words[i-1][-1] != words[i][0]):
            answer = [(i % n) + 1, (i + n) // n]
            break
    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# answer = [3, 3]
print(solution(n, words))

n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
# answer = [0, 0]
print(solution(n, words))

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
# answer = [1, 3]
print(solution(n, words))