# NxM크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시힌다.
# 구멍이 뚫려있는 부분끼리 상,하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오

def DFS(graph, nx, ny, visited):
    dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
    dy = [0, 1, 0, -1]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return False
    if graph[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        for i in range(4):
            DFS(graph, nx+dx[i], ny+dy[i], visited)
        return True
    return False

N, M = map(int, input().split())
graph = []
visited = [[False for _ in range(M)]for _ in range(N)]
cnt = 0
for i in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if DFS(graph, i, j, visited):
            cnt += 1

print(cnt)
