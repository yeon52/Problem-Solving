import math

M, N = map(int, input().split())

is_prime = [True]*(N+1)

for i in range(2,int(math.sqrt(N))+1):
    j=2
    if is_prime[i]:
        while i*j <= N:
            is_prime[i*j] = False
            j += 1

cnt = 0
for i in range(M,N+1):
    if is_prime[i] and i>1:
        print(i)