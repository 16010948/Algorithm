def solution(record):
    answer = []
    MESSAGE = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    name = {}
    for log in record:
        s = log.split()
        if s[0] == "Enter" or s[0] == "Change":
            name[s[1]] = s[2]

    for log in record:
        s = log.split()
        if s[0] != "Change":
            answer.append(name[s[1]] + MESSAGE[s[0]])
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# answer = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(record))