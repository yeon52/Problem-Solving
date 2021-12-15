#특정 거리의 도시 찾기 bfs

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    result = [0]*(N+1);
    q = deque();
    q.append(v);
    visited[v] = True;

    while q:
        v = q.popleft();
        for i in graph[v]:
            if result[i] == 0 and not visited[i]:
                result[i] = result[v]+1;
                q.append(i);

    return result;


N, M, K, X = map(int, input().split());

graph = [[] for _ in range(N+1)];
visited = [False]*(N+1);
for i in range(M):
    a,b = map(int,input().split());
    graph[a].append(b);

result = bfs(X);
isExist = False;
for i in range(1,N+1):
    if result[i]==K:
        isExist=True
        print(i);

if not isExist:
    print(-1);