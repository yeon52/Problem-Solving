# 이중 우선순위 큐
# 힙 사용 X
# def solution(operations):
#     q = []
#     for i in operations:
#         order, num = i.split()
#         if order == 'I':
#             q.append(int(num))
#         elif order == 'D':
#             if q:
#                 if num == '1':
#                     q.pop(q.index(max(q)))
#                 else:
#                     q.pop(q.index(min(q)))
#     if q:
#         answer = [max(q), min(q)]
#     else:
#         answer = [0, 0]
#     return answer

# 힙사용
import heapq


def solution(operations):
    q = []
    for i in operations:
        order, num = i.split()
        if order == 'I':
            heapq.heappush(q, int(num))
        elif order == 'D':
            if q:
                if num == '1':
                    q.remove(heapq.nlargest(1, q)[0])
                else:
                    heapq.heappop(q)
    if q:
        answer = [heapq.nlargest(1, q)[0], heapq.nsmallest(1, q)[0]]
    else:
        answer = [0, 0]
    return answer
