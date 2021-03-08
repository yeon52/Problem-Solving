#N과 M(2), 백트래킹
import sys
import copy
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = True
    result.append(v)

    if depth == M:
        tmp = copy.deepcopy(result)
        tmp.sort()
        if tmp not in ans:
            ans.append(copy.deepcopy(tmp))
            for i in tmp:
                print(i,end=' ')
            print()
        return

    for i in range(1,N+1):
        if not visited[i]:
            dfs(i, depth+1)
            result.pop()
            visited[i] = False

N,M = map(int, input().split())
visited = [False]*(N+1)
ans = []

for i in range(1,N+1):
    result = []
    dfs(i, 1)
    visited[i] = False