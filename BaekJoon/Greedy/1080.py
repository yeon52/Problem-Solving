#1080-그리디, 행렬
def change(A, i, j):
    for m in range(i, i + 3):
        for n in range(j, j + 3):
            A[n][m] = '1' if A[n][m] == '0' else '0'
    return A

N, M = map(int, input().split(" "))
A = []
B = []
for i in range(N):
    A.append(list(input()))
for i in range(N):
    B.append(list(input()))

cnt = 0
for i in range(0, M - 2):
    for j in range(0, N - 2):
        if A[j][i] != B[j][i]:
            change(A,i,j)
            cnt += 1

if A == B:
    print(cnt)
else:
    print('-1')
