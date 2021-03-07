#토마토, dfs/bfs
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
graph = []
dis = [[0]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))

# bfs
q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or graph[nx][ny] != 0:
            continue
        dis[nx][ny] = dis[x][y] + 1
        graph[nx][ny] = 1
        q.append((nx, ny))

result = 0
for i in range(N):
    if 0 in graph[i]:
        result = -1
        break
    result = max(result, max(dis[i]))

print(result)
