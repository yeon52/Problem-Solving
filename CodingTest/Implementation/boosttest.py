#주어진 배열 속 숫자들의 중복횟수를 계산하여 배열로 return, 없다면 -1

import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))
arr_set = set(arr)
result = []
for i in arr_set:
    cnt = arr.count(i)
    if cnt > 1:
        result.append(cnt)

if len(result)==0:
    print(-1)
else:
    print(result)

