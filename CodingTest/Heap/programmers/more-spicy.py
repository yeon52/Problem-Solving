import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        if a >= K and b >= K:
            return answer

        mix = a+b*2
        answer += 1

        heapq.heappush(scoville, mix)

    if scoville and heapq.heappop(scoville) >= K:
        return answer
    else:
        return -1
