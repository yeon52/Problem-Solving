#토마토(3차원), dfs/bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if graph[k][i][j] == 1:
                    q.append((k, i, j))

    while q:
        h, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]
            if nx < 0 or ny < 0 or nh < 0 or nx > N - 1 or ny > M - 1 or nh > H - 1 or graph[nh][nx][ny] != 0:
                continue
            dis[nh][nx][ny] = dis[h][x][y] + 1
            graph[nh][nx][ny] = 1
            q.append((nh, nx, ny))


M,N,H = map(int, input().split())
graph = [[] for _ in range(H)]
dis = [[[0]*M for _ in range(N)]for _ in range(H)]
dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dh = [1,-1,0,0,0,0]

for i in range(H):
    for j in range(N):
        graph[i].append(list(map(int, input().split())))

bfs()

result = 0
for k in range(H):
    for i in range(N):
        if 0 in graph[k][i]:
            result = -1
            break
        result = max(result,max(dis[k][i]))

print(result)