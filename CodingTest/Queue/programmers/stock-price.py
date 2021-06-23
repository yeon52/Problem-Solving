# 주식 가격
# 2중포문 - O(n^2)
# def solution(prices):
#     result = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             cnt+=1
#             if prices[i]>prices[j]:
#                 break
#         result.append(cnt)
#     return result

# 스택 이용
from collections import deque


def solution(prices):
    result = [0]*len(prices)
    q = deque()
    for i, price in enumerate(prices):
        while q and prices[q[-1]] > price:  # 값이 떨어지면
            j = q.pop()
            result[j] = i-j
        q.append(i)

    while q:
        j = q.pop()
        result[j] = len(prices)-j-1

    return result
