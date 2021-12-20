#위상정렬 이용

import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
q = []
result = []

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] +=1

for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i);

while q:
    n = heapq.heappop(q);
    result.append(n)

    for i in graph[n]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i);

for i in result:
    print(i, end=' ')