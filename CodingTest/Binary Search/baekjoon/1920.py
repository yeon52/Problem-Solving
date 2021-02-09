#  이진탐색 알고리즘 구현
# def is_exist(arr, target):  # binary search
#     start = 0
#     end = N-1
#     while start <= end:
#         mid = (start + end) // 2
#         if target == arr[mid]:
#             return 1
#         if target < arr[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#
#     return 0
#
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))
# A.sort()
# for i in B:
#     print(is_exist(A,i))

## bisect 라이브러리 사용

from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for i in B:
    left_index = bisect_left(A,i)
    right_index = bisect_right(A,i)
    result = right_index - left_index
    if result > 0:
        print(1)
    else:
        print(0)
