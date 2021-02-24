#연속 합
# n = int(input())
# arr = list(map(int, input().split()))
# end = 0
# sum = 0
# result = arr[0]
#
# for end in range(n):
#     sum += arr[end]
#     result = max(result,sum)
#
#     if sum < 0:
#         sum = 0
#
# print(result)

#위 코드로 짰는데.. (통과함, 해결법은 같음) 알고보니 dp문제였다..
#dp 코드

n = int(input())
arr = list(map(int, input().split()))
d = [0]*n
d[0] = arr[0]

for i in range(1,n):
    d[i] = max(d[i-1]+arr[i], arr[i])

print(max(d))