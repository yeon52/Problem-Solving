# 최대공약수와 최소공배수

# 개념 그대로 풀이
# n, m = map(int, input().split())
# gcd, lcm = 0, 0
# if n>m:
#     n,m = m,n
#
# for i in range(1,n+1):
#     if n%i == 0 and m%i == 0:
#         gcd = i
#
# j=m
# k = 1
# while True:
#     m = j*k
#     if m%n == 0:
#         lcm = m
#         break
#     k+=1
#
# print(gcd)
# print(lcm)


# 유클리드 호제법
n, m = map(int, input().split())
if n > m:
    n, m = m, n


def gcd(A, B):
    if A % B == 0:
        return B
    else:
        return gcd(B, A % B)


gcd = gcd(n, m)
lcm = (n*m) // gcd

print(gcd)
print(lcm)
