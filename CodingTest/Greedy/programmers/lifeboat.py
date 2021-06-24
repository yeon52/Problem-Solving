#그리디, 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1

    while start < end:
        s = people[start] + people[end]
        if s <= limit:
            answer += 1
            start += 1
            end -= 1
        elif s > limit:
            answer += 1
            end -= 1
    if start == end:
        answer += 1
    return answer
