import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

end, interval_sum = 0, 0
cnt = 0
min_cnt = 100000001

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += arr[end]
        end += 1
        cnt += 1

    if interval_sum >= M and cnt < min_cnt:
        min_cnt = cnt

    interval_sum -= arr[start]
    cnt -= 1

if min_cnt == 100000001:
    print(0)
else:
    print(min_cnt)