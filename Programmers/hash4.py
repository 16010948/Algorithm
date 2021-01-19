def solution(genres, plays):
    answer = []
    total = {}
    index = {}

    for i in range(len(genres)):
        if genres[i] in total.keys():
            total[genres[i]] += plays[i]
            index[genres[i]][i] = plays[i]
        else:
            total[genres[i]] = plays[i]
            index[genres[i]] = {i: plays[i]}

    sorted_total = sorted(total.items(), reverse=True, key=lambda item: item[1])

    for genre in sorted_total:
        for i in sorted(index[genre[0]].items(), reverse=True, key=lambda item: item[1])[:2]:
            answer.append(i[0])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# answer = [4, 1, 3, 0]
print(solution(genres, plays))