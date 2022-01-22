INF = int(1e9)
keyboard = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8),
    'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
}
VOWEL = "yuiophjklbnm"

def is_vowel(char):
    return char in VOWEL

def calc_distance(target, cur):
    return abs(keyboard[target][0] - keyboard[cur][0]) + abs(keyboard[target][1] - keyboard[cur][1])

left, right = input().split()
word = input()

answer = 0
for char in word:
    if is_vowel(char):
        answer += calc_distance(char, right) + 1
        right = char
    else:
        answer += calc_distance(char, left) + 1
        left = char
print(answer)