s = input()
word = input()

s_length = len(s)
w_length = len(word)
answer = 0
i = 0
while i <= s_length - w_length:
    if s[i] == word[0]:
        is_correct = True
        for j in range(1, w_length):
            if s[i + j] != word[j]:
                is_correct = False
                break

        if is_correct:
            i += w_length - 1
            answer += 1
    i += 1
print(answer)