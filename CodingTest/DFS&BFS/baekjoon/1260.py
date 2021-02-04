#dfs와 bfs
from collections import deque

def dfs(graph, v, visited):
    visited.append(v)
    print(v, end=" ")
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

n, m, v = map(int, input().split())
p = [[] for _ in range(n + 1)]
visited = []
for i in range(m):
    a, b = map(int, input().split())
    p[a].append(b)
    p[b].append(a)
for i in range(n+1):
    p[i].sort()

dfs(p, v, visited)
print()
visited = []
bfs(p, v, visited)
