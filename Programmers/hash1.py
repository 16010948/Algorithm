def solution(participant, completion):
    answer = ''
    participants = {}

    for p in participant:
        if p in participants.keys():
            participants[p] += 1
        else:
            participants[p] = 1

    for c in completion:
        participants[c] -= 1

    for p in participants:
        if participants[p] > 0:
            answer = p
            break

    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
# answer = "leo"
print("#1", solution(participant, completion))

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
# answer = "vinko"
print("#2", solution(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# answer = "mislav"
print("#3", solution(participant, completion))