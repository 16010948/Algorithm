def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        count = 0
        flag = True
        for s in skill_tree:
            if s in skill:
                if skill.index(s) == count:
                    count += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# answer = 2
print(solution(skill, skill_trees))