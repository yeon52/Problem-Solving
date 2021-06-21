#프린터, 큐
from collections import deque


def solution(priorities, location):
    #q = deque()
    # for i in range(len(priorities)):
    #    q.append((priorities[i], i))
    q = deque([(p, l) for l, p in enumerate(priorities)])
    # 인덱스를 함께 다루고 싶을 땐 enumerate!
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
