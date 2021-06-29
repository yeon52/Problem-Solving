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
# import heapq

# def solution(operations):
#     q = []
#     for i in operations:
#         order, num = i.split()
#         if order == 'I':
#             heapq.heappush(q, int(num))
#         elif order == 'D':
#             if q:
#                 if num == '1':
#                     q.remove(heapq.nlargest(1, q)[0])
#                 else:
#                     heapq.heappop(q)
#     if q:
#         answer = [heapq.nlargest(1, q)[0], heapq.nsmallest(1, q)[0]]
#     else:
#         answer = [0, 0]
#     return answer

# 힙사용 다른풀이 -----위 방법들은 백준에서는 시간초과 뜸. 이건통과 -------
# 힙 두개 사용하여 연동
import heapq
import sys
input = sys.stdin.readline


def solution(operations):
    maxh = []
    minh = []
    visited = [False] * 1000001

    for i in range(len(operations)):
        order, num = operations[i].split()
        if order == 'I':
            heapq.heappush(minh, (int(num), i))  # id 함께 저장
            heapq.heappush(maxh, (-int(num), i))
            visited[i] = True
        elif order == 'D':
            if num == '1':
                while maxh and not visited[maxh[0][1]]:  # 다른곳에서 지워진 수 체크해서 지우기
                    heapq.heappop(maxh)
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)
            else:
                while minh and not visited[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)

    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)
    while minh and not visited[minh[0][1]]:
        heapq.heappop(minh)
    if minh:
        answer = str(-maxh[0][0]) + ' ' + str(minh[0][0])
    else:
        answer = 'EMPTY'

    return answer


T = int(input())
ans = []
for i in range(T):
    n = int(input())
    operation = []
    answer = ''
    for i in range(n):
        operation.append(input())

    ans.append(solution(operation))

for i in ans:
    print(i)
