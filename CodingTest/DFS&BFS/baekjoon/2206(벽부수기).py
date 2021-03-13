# 벽부수고 이동하기, bfs

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, c):  # c는 벽부순 여부 체크. 0배열이 안부숨, 1이 부숨
    q = deque()
    q.append((x, y, c))
    visited[x][y][c] = 1
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내 & 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][c] == 0:
                if graph[nx][ny] == 1 and c == 0:  # 벽인데 한번도 안부순 경우
                    visited[nx][ny][1] = visited[x][y][c] + 1  # 부수면서 경로 +1
                    q.append((nx, ny, 1))  # 부순거와 함께 q 삽입

                elif graph[nx][ny] == 0:  # 벽이 아닌경우
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append((nx, ny, c))


N, M = map(int, input().split())
graph = []
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]  # x좌표, y좌표, 벽 부순 여부
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

bfs(0, 0, 0)

a = visited[N-1][M-1][0]
b = visited[N-1][M-1][1]

if a == 0 and b == 0:
    print(-1)
elif a == 0 or b == 0:
    print(max(a, b))
else:
    print(min(a, b))
