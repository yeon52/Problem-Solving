# NxM 크기의 직사각형 형태의 미로. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야한다.
# 시작위치는 (1,1), 출구는 (N,M) 이며 한번에 한칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0, 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시됨.
# 이때 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
from collections import deque

def bfs(m,x,y):
    queue = deque()
    queue.append((x,y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>N-1 or ny>M-1:
                continue
            if m[nx][ny] == 1:
                m[nx][ny] = m[x][y] + 1
                queue.append((nx,ny))
    return m[N-1][M-1]

N, M = map(int, input().split())
m = []
for i in range(N):
    m.append(list(map(int, input())))

print(bfs(m, 0, 0))