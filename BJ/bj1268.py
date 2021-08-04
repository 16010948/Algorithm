n = int(input())

classes = [{} for _ in range(5)]
for i in range(n):
    students = list(map(int, input().split()))
    for grade in range(5):
        if students[grade] in classes[grade]:
            classes[grade][students[grade]].append(i + 1)
        else:
            classes[grade][students[grade]] = [i + 1]

friends = [set() for _ in range(n + 1)]
max_friends = 0
leader = 0
for dic in classes:
    for key in dic:
        for c in dic[key]:
            friends[c] = friends[c].union(set(dic[key]))
            if len(friends[c]) > max_friends:
                max_friends = len(friends[c])
                leader = c
print(leader)