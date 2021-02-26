#유기농 배추
import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, x, y):
    q = deque()
    if graph[x][y] == 0 or x<0 or y<0 or x>N-1 or y>M-1:
        return False
    q.append((x,y))
    graph[x][y] = 0 #방문처리

    while q:
        x, y = q.popleft()
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>N-1 or ny>M-1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

    return True

T = int(input())
result = []
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(N):
        for j in range(M):
            if bfs(graph, i, j):
                cnt +=1

    result.append(cnt)

for i in result:
    print(i)
