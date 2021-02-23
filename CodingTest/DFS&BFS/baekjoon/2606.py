#바이러스

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited.append(v)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i not in visited:
                q.append(i)
                visited.append(i)

N = int(input())
M = int(input())
computer = [[] for _ in range(N+1)]
visited = []
for i in range(M):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

bfs(computer, 1, visited)

print(len(visited)-1)