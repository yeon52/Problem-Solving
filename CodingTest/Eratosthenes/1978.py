import math

N = int(input())
val = list(map(int, input().split()))
m = max(val)
is_prime = [True]*(m+1)

for i in range(2,int(math.sqrt(m))+1):
    j=2
    if is_prime[i]:
        while i*j <= m:
            is_prime[i*j] = False
            j += 1

cnt = 0
for i in val:
    if is_prime[i] and i>1:
        cnt+=1
print(cnt)