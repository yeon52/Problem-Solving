import sys
from collections import deque
input = sys.stdin.readline

#bfs

def bfs(n,k):
    if n==k:
        return 0
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        n = q.popleft()
        move = [n - 1, n + 1, 2 * n]
        for i in move:
            if i < 0 or i > 100000 or visited[i]:
                continue
            if i == k:
                sec[i] = sec[n]+1
                return sec[i]

            visited[i] = True
            q.append(i)
            sec[i] = sec[n] + 1

N, K = map(int, input().split())
result = 0
visited = [False]*100001
sec = [0]*100001

print(bfs(N,K))







#dp