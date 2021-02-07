# 배열 A,B는 N개의 원소로 구성되어 있으며 모두 자연수이다.
# 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란
# 배열 A에 있는 원소하나와 배열 B에 있는 원소 하나를 골라서 서로 바꾸는 것이다.
# N,K 그리고 배열 A, B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

N, K = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))