#프린터, 큐
from collections import deque


def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    print_ = 0

    while q:
        maxP = max(q)[0]
        p, locate = q.popleft()
        if p == maxP:
            print_ += 1
            if locate == location:
                return print_
        else:
            q.append((p, locate))
