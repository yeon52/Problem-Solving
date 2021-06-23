# 소수
import math
M = int(input())
N = int(input())

is_prime = [True]*(N+1)
cnt = 0
result = []
for i in range(2, int(math.sqrt(N))+1):
    j = 2
    if is_prime[i]:
        while i*j <= N:
            is_prime[i*j] = False
            j += 1

for i in range(M, N+1):
    if is_prime[i] and i > 1:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
