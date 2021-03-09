# 스타트와 링크, 백트래킹(itertools 사용)
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
S = []
p = [i for i in range(1, N+1)]
result = 1e9

for i in range(N):
    S.append(list(map(int, input().split())))
c = list(combinations(p, N//2))

for k in range(len(c)//2):
    a = c[k]
    b = c[len(c)-k-1]
    a_sum = b_sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            a_sum += S[a[i]-1][a[j]-1]+S[a[j]-1][a[i]-1]
            b_sum += S[b[i]-1][b[j]-1]+S[b[j]-1][b[i]-1]
    sub = a_sum - b_sum
    result = min(result, abs(sub))

print(result)
