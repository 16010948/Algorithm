def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        lower_city = city.lower()
        if lower_city not in cache:
            answer += 5
            cache.append(lower_city)
            if len(cache) > cacheSize:
                cache.pop(0)
        else:
            answer += 1
            cache.append(lower_city)
            cache.remove(lower_city)

    return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# answer = 50
print(solution(cacheSize, cities))

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
# answer = 21
print(solution(cacheSize, cities))

cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# answer = 60
print(solution(cacheSize, cities))

cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# answer = 52
print(solution(cacheSize, cities))

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
# answer = 16
print(solution(cacheSize, cities))

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# answer = 25
print(solution(cacheSize, cities))