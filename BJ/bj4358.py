import sys
input = sys.stdin.readline

trees ={}
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    n += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

sorted_trees = sorted(trees.keys())
for tree_name in sorted_trees:
    print("%s %.4f" % (tree_name, (trees[tree_name] /n) * 100))