# 연산자 끼워넣기, 백트래킹, dfs

import sys
input = sys.stdin.readline


def recursive(i, res, add, sub, mul, div):
    global rmax, rmin

    if i == N:
        rmax = max(res, rmax)
        rmin = min(res, rmin)
        return

    if add:
        recursive(i+1, res+num[i], add-1, sub, mul, div)
    if sub:
        recursive(i+1, res-num[i], add, sub-1, mul, div)
    if mul:
        recursive(i+1, res*num[i], add, sub, mul-1, div)
    if div:
        if res < 0:
            recursive(i + 1, -(-res // num[i]), add, sub, mul, div - 1)
        else:
            recursive(i+1, res//num[i], add, sub, mul, div-1)


N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
global rmax, rmin
rmax = -1e9
rmin = 1e9

recursive(1, num[0], add, sub, mul, div)

print(rmax)
print(rmin)

# 시간초과 - 같은값이 여러가지일때 같은 연산을 여러번 해서 비효율적임
# import sys
# input = sys.stdin.readline
#
# def dfs(v):
#     visited[v] = True
#     result.append(operator[v])
#
#     for i in range(N-2):
#         if not visited[i] and operator[i]!=operator[i+1]:
#             dfs(i)
#             result.pop()
#             visited[i] = False
#
#     if len(result)==N-1:
#         tmp = num[0]
#         for i in range(N-1):
#             if result[i] == '+':
#                 tmp = tmp+num[i+1]
#             elif result[i] == '-':
#                 tmp = tmp-num[i+1]
#             elif result[i] == 'x':
#                 tmp = tmp*num[i+1]
#             else:
#                 if tmp<0:
#                     tmp = - (-tmp//num[i+1])
#                 else:
#                     tmp = tmp//num[i+1]
#
#         ans.append(tmp)
#
# N = int(input())
# num = list(map(int, input().split()))
# cnt = list(map(int, input().split()))
# visited = [False]*(N-1)
# ans = []
# result = []
# operator = list('+'*cnt[0]+'-'*cnt[1]+'x'*cnt[2]+'/'*cnt[3])
#
# for i in range(N-1):
#     result = []
#     dfs(i)
#     visited[i] = False
#
# print(max(ans))
# print(min(ans))
