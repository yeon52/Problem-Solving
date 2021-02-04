#dfs, 섬의 개수
import sys
sys.setrecursionlimit(10**6)

def dfs(m,x,y):
    if x<0 or y<0 or x>h-1 or y>w-1:
        return False
    dx = [1,-1,0,0,-1,-1,1,1]  # 상, 하, 좌,우, 대각선
    dy = [0,0,1,-1,-1,1,-1,1]
    if m[x][y] == 1:
        m[x][y] = 0
        for i in range(8):
            dfs(m,x+dx[i],y+dy[i])
        return True
    return False

result = []
while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    m = []
    cnt = 0
    for i in range(h):
        m.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if dfs(m, i, j):
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)



#### bfs 이용 #####
# from collections import deque
# def bfs(m, x, y):
#     if x<0 or y<0 or x>h-1 or y>w-1 or m[x][y]==0:
#         return False
#     queue = deque()
#     queue.append((x, y))
#     dx = [1, -1, 0, 0, 1, -1, 1, -1]
#     dy = [0, 0, 1, -1, 1, -1, -1, 1]
# 
#     while queue:
#         x, y = queue.popleft()
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1:
#                 continue
#             elif m[nx][ny] == 1:
#                 m[nx][ny] = 0
#                 queue.append((nx,ny))
#     return True
# 
# result = []
# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
#     m = []
#     cnt = 0
#     for i in range(h):
#         m.append(list(map(int, input().split())))
#     for i in range(h):
#         for j in range(w):
#             if bfs(m, i, j):
#                 cnt += 1
#     result.append(cnt)
# 
# for i in result:
#     print(i)
