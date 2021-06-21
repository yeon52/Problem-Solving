# 다리를 지나는 트럭, 큐

from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    q_ing = deque([0 for _ in range(bridge_length)])
    sec = 0
    sum_t = 0
    while q:
        sum_t -= q_ing.popleft()
        sec += 1
        if sum_t+q[0] <= weight:
            t = q.popleft()
            q_ing.append(t)
            sum_t += t
        else:
            q_ing.append(0)

    while q_ing:
        q_ing.popleft()
        sec += 1

    return sec
