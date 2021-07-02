# 캐쉬, LRU알고리즘, 2018 kakao blind recruitment
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        answer = len(cities)*5

    else:
        for city in cities:
            city = city.lower()
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                if len(cache) == cacheSize:
                    cache.popleft()
                    cache.append(city)
                    answer += 5
                else:
                    cache.append(city)
                    answer += 5
    return answer
