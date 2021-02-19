import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    queue = deque()
    for i in range(1,N+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        n = queue.popleft()
        result.append(n)
        for i in graph[n]:
            indegree[i]-=1
            if indegree[i] == 0:
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
result = []

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

topology_sort()

for i in range(N):
    print(result[i],end=" ")
