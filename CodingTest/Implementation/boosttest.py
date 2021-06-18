#주어진 배열 속 숫자들의 중복횟수를 계산하여 배열로 return, 없다면 -1

import sys

input = sys.stdin.readline

def countOf(n):
    return arr.count(n)

arr = list(map(int, input().split()))
arr.sort()
arr2 = set(arr)
arr2 = list(arr2)
result = []
for i in arr2:
    t = countOf(i)
    if t>1:
        result.append(t)

if len(result)==0:
    print(-1)
else:
    print(result)

#다른풀이
# pre = arr[0]
# result=[]
# cnt = 1
# for i in arr[1:]:
#     if pre == i:
#         cnt += 1
#     elif cnt > 1:
#         result.append(cnt)
#         cnt = 1
#     pre = i
#
# if cnt>1:
#     result.append(cnt)
#
# if len(result)==0:
#     print(-1)
# else:
#     print(result)
