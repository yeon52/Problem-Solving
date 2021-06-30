# A->B, bfs
import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
q = deque()
i = 0
q.append((A, 0))
result = -1
while q:
    n, i = q.popleft()
    if n == B:
        result = i+1
        break
    if 2*n <= B:
        q.append((2*n, i+1))
    if int(str(n)+'1') <= B:
        q.append((int(str(n)+'1'), i+1))

print(result)
