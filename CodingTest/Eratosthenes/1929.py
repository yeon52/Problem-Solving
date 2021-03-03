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

# 소수판별

# import math

# def is_prime_number(x):
#     for i in range(2,int(math.sqrt(x))+1):
#         if x%i == 0:
#             return False #2이상의 수로 나누어 떨어짐 -> 소수 아님
#     return True #소수