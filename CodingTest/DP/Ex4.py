# nxm크기의 금광이 있다. 금광은 1x1 크기의 칸으로 나누어져 있으며, 각 칸은 특정크기의 금이 들어있다.
# 채굴자는 첫번째 열부터 출발하여 금을 캐기 시작한다.
# 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다.
# 이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요

#보텀업
t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    d = [[0]*m for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(m):
            d[i][j] = line[k]
            k+=1

    for j in range(1,m):
        for i in range(n):
            if i==0:
                d[i][j] = max(d[i][j - 1], d[i + 1][j - 1]) + d[i][j]
            elif i==n-1:
                d[i][j] = max(d[i - 1][j - 1], d[i][j - 1]) + d[i][j]
            else:
                d[i][j] = max(d[i-1][j-1],d[i][j-1],d[i+1][j-1]) + d[i][j]

    tmp = 0
    for i in range(n):
        tmp = max(tmp,d[i][m-1])
    result.append(tmp)

for i in result:
    print(i)