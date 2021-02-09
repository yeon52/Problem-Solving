# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이때 이 수열에서 x가 등장하는 횟수를 계산하라

## 1 <= N <= 1,000,000 이므로 logN 복잡도만 가능 ##

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
n = list(map(int, input().split()))

right_index = bisect_right(n, x)
left_index = bisect_left(n, x)

result = right_index - left_index
if result == 0:
    print(-1)
else:
    print(right_index-left_index)
