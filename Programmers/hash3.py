def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]

    for c in closet:
        answer *= (len(closet[c]) + 1)

    return answer - 1

clothes = [["yellow_hat", "headgear"],
           ["blue_sunglasses", "eyewear"],
           ["green_turban", "headgear"]]
# answer = 5
print("#1", solution(clothes))

clothes = [["crow_mask", "face"],
           ["blue_sunglasses", "face"],
           ["smoky_makeup", "face"]]
# answer = 3
print("#2", solution(clothes))