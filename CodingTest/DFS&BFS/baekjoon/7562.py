# 나이트의 이동, bfs
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, -2, -1, 2, 1]
result = []


def bfs(x, y, rx, ry):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == rx and ny == ry:
                graph[nx][ny] = graph[x][y] + 1
                return
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))


for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    rx, ry = map(int, input().split())
    graph = [[0]*n for _ in range(n)]

    if x == rx and y == ry:
        result.append(0)
    else:
        bfs(x, y, rx, ry)
        result.append(graph[rx][ry])

for i in result:
    print(i)
