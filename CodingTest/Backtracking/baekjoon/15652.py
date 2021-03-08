# N과 M(4), 백트래킹

import sys
input = sys.stdin.readline


def dfs(v, depth):
    result.append(v)

    if depth == M:
        for i in result:
            print(i, end=' ')
        print()
        return

    for i in range(v, N+1):
        dfs(i, depth+1)
        result.pop()


N, M = map(int, input().split())
visited = [False]*(N+1)

for i in range(1, N+1):
    result = []
    dfs(i, 1)
