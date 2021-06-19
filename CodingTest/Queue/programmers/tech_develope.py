#기술개발/ 스택,큐
import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        queue.append(math.ceil((100-progresses[i])/speeds[i]))

    cnt = 1
    pre = queue.popleft()
    while queue:
        release = queue.popleft()
        if release<=pre:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
        pre = max(release,pre)

    answer.append(cnt)
    return answer