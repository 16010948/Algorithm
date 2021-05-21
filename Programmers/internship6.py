import re


def solution(user_id, banned_id):
    answer = []

    filtered = [[]]
    for mask in banned_id:
        mask = mask.replace('*', '\w')
        cur_filtered = []
        for user in user_id:
            if re.fullmatch(mask, user):
                for users in filtered:
                    if user not in users:
                        cur_filtered.append(users + [user])
        filtered = cur_filtered

    for users in filtered:
        if set(users) not in answer:
            answer.append(set(users))

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
# answer = 2
print(solution(user_id, banned_id))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
# answer = 2
print(solution(user_id, banned_id))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
# answer = 3
print(solution(user_id, banned_id))