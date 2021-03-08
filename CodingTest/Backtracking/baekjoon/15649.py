#N과 M(1), 백트래킹
import sys
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = True
    result.append(v)

    if depth == M:
        for i in result:
            print(i, end=' ')
        print()
        return

    for i in range(1,N+1):
        if not visited[i]:
            dfs(i, depth+1)
            result.pop()
            visited[i] = False

N,M = map(int, input().split())
visited = [False]*(N+1)

for i in range(1,N+1):
    result = []
    dfs(i, 1)
    visited[i] = False