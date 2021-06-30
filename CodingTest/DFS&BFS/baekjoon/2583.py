# 영역 구하기, bfs

from collections import deque


def bfs(m, x, y):
    if m[x][y] == 1:
        return -1
    q = deque()
    q.append((x, y))
    m[x][y] = 1
    cnt = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > M - 1 or ny > N - 1 or nx < 0 or ny < 0 or m[nx][ny] == 1:
                continue
            q.append((nx, ny))
            m[nx][ny] = 1
            cnt += 1

    return cnt


M, N, K = map(int, input().split())
m = [[0]*N for _ in range(M)]
result = []

for i in range(K):
    lx, ly, rx, ry = map(int, input().split())

    for j in range(ly, ry):
        for k in range(lx, rx):
            m[j][k] = 1

for i in range(M):
    for j in range(N):
        tmp = bfs(m, i, j)
        if tmp > 0:
            result.append(tmp)
result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
