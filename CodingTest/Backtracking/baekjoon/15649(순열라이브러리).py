# N과 M(1), 백트래킹
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

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i, depth+1)
            result.pop()
            visited[i] = False


N, M = map(int, input().split())
visited = [False]*(N+1)

for i in range(1, N+1):
    result = []
    dfs(i, 1)
    visited[i] = False

# 순열 라이브러리 사용
# import sys
# from itertools import permutations
# input = sys.stdin.readline
#
# N,M = map(int, input().split())
# li = []
# for i in range(1,N+1):
#     li.append(i)
# perm = permutations(li,M)
#
# for i in perm:
#     a =[str(p) for p in i]
#
#     print(' '.join(a))
