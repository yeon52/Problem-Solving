# 11047 - 그리디, 동전 0

N, K = map(int, input().split(" "))
coin = [0] * N
cnt = 0

for i in range(N):
    coin[i] = int(input())

for i in reversed(coin):
    if i <= K:
        cnt += K // i
        K = K % i
        if K == 0:
            break

print(cnt)
