# 큰 수 만들기, 그리디
from collections import deque


def solution(number, k):
    cnt = 0
    num = deque(number)
    ans = deque()
    while num:
        a = num.popleft()
        while ans and cnt < k and a > ans[-1]:
            ans.pop()
            cnt += 1
        ans.append(a)

    while cnt < k:
        ans.pop()
        cnt += 1

    return ''.join(ans)
