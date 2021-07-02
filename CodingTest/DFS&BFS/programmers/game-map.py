# 게임 맵 최단거리, bfs

# bfs풀이
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    result = -1
    q = deque()
    q.append((0, 0, 1))
    maps[0][0] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y, path = q.popleft()
        if x == n-1 and y == m-1:
            result = path
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny, path+1))
                maps[nx][ny] = 0

    return result

# dfs로도 풀어봤지만 효율성에서 실패! --> 최단거리문제는 bfs로 풀자 !
# import sys
# sys.setrecursionlimit(10**6)
# min_path = 10001
# def bfs(maps, x, y, depth, n, m):
#     global min_path
#     if x==n-1 and y==m-1:
#         min_path = min(min_path, depth)
#         return
#     maps[x][y] = 0
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
#             maps[nx][ny] = 0
#             bfs(maps, nx, ny, depth+1, n, m)
#             maps[nx][ny] = 1

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     result = -1
#     bfs(maps, 0,0,1, n, m)
#     if min_path != 10001:
#         result = min_path
#     return result
