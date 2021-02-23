import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
visited = [False]*26
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
global max_cnt
max_cnt = 1
def dfs(x,y, cnt):
    global max_cnt
    visited[ord(graph[x][y])-65] = True
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > R - 1 or ny > C - 1:
            continue
        if not visited[ord(graph[nx][ny])-65]:
            dfs(nx,ny,cnt+1)
            visited[ord(graph[nx][ny])-65] = False

for i in range(R):
    graph.append(list(input().rstrip()))

dfs(0,0,max_cnt)

print(max_cnt)
