#N-Queen
import sys

N = int(input())
col, slash, backslash = [False]*N, [False]*2*N, [False]*2*N
global result
result = 0
def solve(i):
    global result
    if i==N:
        result+=1
        return
    for j in range(N):
        if not (col[j] or slash[i+j] or backslash[i-j+N-1]):
            col[j] = slash[i+j] = backslash[i-j+N-1] = True
            solve(i+1)
            col[j] = slash[i + j] = backslash[i - j + N - 1] = False
solve(0)

print(result)