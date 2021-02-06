#단지번호 붙이기, bfs & dfs

from collections import deque

def bfs(graph,x,y,cnt):
    if x<0 or y<0 or x>N-1 or y>N-1 or graph[x][y]==0:
        return -1
    queue = deque()
    queue.append((x,y))
    cnt +=1
    graph[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1 or graph[nx][ny] == 0:
                continue
            queue.append((nx,ny))
            graph[nx][ny] = 0
            cnt +=1
    return cnt

N = int(input())
graph = []
cnt = 0
result = []
for i in range(N):
    graph.append(list(map(int,input())))

for i in range(N):
    for j in range(N):
        a = bfs(graph,i,j,0)
        if a != -1:
            cnt += 1
            result.append(a)
result.sort()
print(cnt)
for i in range(len(result)):
    print(result[i])


###dfs 사용###

# def dfs(graph, x, y, cnt):
#     if x < 0 or y < 0 or x > N - 1 or y > N - 1 or graph[x][y] == 0:
#         return -1
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     graph[x][y] = 0
#     cnt += 1
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1 or graph[nx][ny] == 0:
#             continue
#         cnt = dfs(graph, nx, ny, cnt)
#     return cnt

# N = int(input())
# graph = []
# cnt = 0
# result = []
# for i in range(N):
#     graph.append(list(map(int, input())))

# for i in range(N):
#     for j in range(N):
#         a = dfs(graph,i,j,0)
#         if a != -1:
#             cnt += 1
#             result.append(a)
# result.sort()
# print(cnt)
# for i in range(len(result)):
#     print(result[i])