class Trie:
    class Node:
        def __init__(self, key, depth, count=0, data=None):
            self.key = key
            self.depth = depth
            self.data = data
            self.count = 0
            self.children = {}

    def __init__(self):
        self.root = self.Node(None, 0)

    def insert(self, string):
        cur_node = self.root
        for char in string:
            cur_node.count += 1
            if char not in cur_node.children:
                cur_node.children[char] = self.Node(char, cur_node.depth + 1)
            else:
                cur_node.children[char].count += 1
            cur_node = cur_node.children[char]
        cur_node.data = string

    def traversal_minimum_character(self, string):
        cur_node = self.root

        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                if cur_node.count == 1:
                    break

        return cur_node.depth


def solution(words):
    answer = 0

    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.traversal_minimum_character(word)

    return answer

words = ["go", "gone", "guild"]
# answer = 7
print(solution(words))

words = ["abc", "def", "ghi", "jklm"]
# answer = 4
print(solution(words))

words = ["word", "war", "warrior", "world"]
# answer = 15
print(solution(words))