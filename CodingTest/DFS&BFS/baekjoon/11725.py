#트리의 부모 찾기
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                parent[i] = v
                q.append(i)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
parent = [0]*(N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

for i in range(2,N+1):
    print(parent[i])
