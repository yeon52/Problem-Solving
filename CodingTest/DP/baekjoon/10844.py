#쉬운계단수
#DP

d = [[0]*10 for _ in range(101)]
N = int(input())
result = 0

for i in range(1,10):
    d[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        if j==0:
            d[i][j] = d[i - 1][j + 1]
        elif j==9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

for i in range(10):
    result += d[N][i]

print(result%1000000000)
