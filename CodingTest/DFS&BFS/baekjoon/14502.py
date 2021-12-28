#bfs
from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline;

def bfs(graph2, x,y):
    q = deque();
    q.append((x,y));
    dx = [0,0,1,-1];
    dy = [1,-1,0,0];
    while q:
        x, y = q.popleft();
        for i in range(4):
            nx = x + dx[i];
            ny = y + dy[i];
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or graph2[nx][ny] != 0:
                continue
            graph2[nx][ny] = 2
            q.append((nx,ny));

def countZero(graph2):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph2[i][j] == 0:
                cnt+=1;
    return cnt;

N, M = map(int, input().split());
graph = [];
location = [];
result = 0;
for i in range(N):
    graph.append(list(map(int, input().split())));

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            location.append((i,j));

wallLocate = list(combinations(location, 3));
for i in wallLocate:
    graph2 = copy.deepcopy(graph);
    for x,y in i:
        graph2[x][y] = 1;
    for j in range(N):
        for k in range(M):
            if graph2[j][k] == 2:
                bfs(graph2, j, k)
    result = max(result, countZero(graph2));

print(result);