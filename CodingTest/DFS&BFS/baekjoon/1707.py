#이분그래프, bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == visited[v]:
                return False
            if visited[i] == 0:
                if visited[v] == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
                q.append(i)
    return True

K = int(input())
result = []

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0]*(V+1) #0이면 방문 X, 1과 2로 두 그룹 나누기

    for i in range(E):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    chk = 0
    for i in range(1,V+1):
        if visited[i]==0:
            if not bfs(i):
                chk = 1
                break
    if chk == 1:
        result.append('NO')
    else:
        result.append('YES')

for i in result:
    print(i)