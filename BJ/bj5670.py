import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.child = {}
        self.is_last_char = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for char in word:
            if char not in cur.child:
                cur.child[char] = Node()
            cur = cur.child[char]
        cur.is_last_char = True

    def find(self, word):
        cur = self.root
        count = 0
        for char in word:
            cur = cur.child[char]
            if len(cur.child) >= 2 or cur.is_last_char:
                count += 1
        return count

while True:
    try:
        n = int(input())

        words = []
        trie = Trie()
        for i in range(n):
            words.append(input().strip())
            trie.insert(words[i])

        answer = 0
        for i in range(n):
            answer += trie.find(words[i])
        print("%.2f" % (answer / n))

    except:
        break