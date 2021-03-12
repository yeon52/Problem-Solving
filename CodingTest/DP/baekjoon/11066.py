import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    K = int(input())
    page = list(map(int, input().split()))
    d = [[0]*(K+1) for _ in range(K+1)]
    sum_ = [0]*(K+1)

    for i in range(1, K+1):
        sum_[i] = sum_[i-1]+page[i-1]

    for gap in range(1, K):
        for start in range(1, K-gap+1):
            end = start+gap
            d[start][end] = 1e9
            for mid in range(start, end):
                d[start][end] = min(
                    d[start][end], d[start][mid]+d[mid+1][end] + sum_[end]-sum_[start-1])

    ans.append(d[1][K])

for i in ans:
    print(i)
