n = int(input())

school_classes = [[] for _ in range(5)]
for i in range(n):
    school_class = list(map(int, input().split()))
    for j in range(5):
        school_classes[j].append(school_class[j])

students = [set()] * n
# for i in range(5):
#     for j in range(n):
#         if school_classes[i][j] in headcount.keys():
#             students[j].append(j)
#         else:
#             students[school_classes[i][j]] = [j]
#     print(headcount)
    # for j in range(n):
    #     students[j] += headcount[school_classes[i][j]]
    #     if max_headcount < students[j]:
    #         max_headcount = students[j]
    #         class_leader = j
# print(class_leader + 1)