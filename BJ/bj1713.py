n = int(input())
m = int(input())

recommend = list(map(int, input().split()))
vote = {}
candidate = []
for r in recommend:
    if r in candidate:
        vote[r] += 1
    else:
        if len(candidate) >= n:
            min_vote = int(1e9)
            min_candidate = 0
            for c in candidate:
                if vote[c] < min_vote:
                    min_candidate = c
                    min_vote = vote[c]
            candidate.remove(min_candidate)
            vote[min_candidate] = 0
        candidate.append(r)
        vote[r] = 1
candidate.sort()
print(" ".join(map(str, candidate)))