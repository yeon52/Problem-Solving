# 디스크 컨트롤러, 힙
import heapq


def solution(jobs):
    h = []
    jobs.sort()
    cur_time = 0
    cur_index = 0
    ever = 0
    i = 0
    ask_time = 0
    while i < len(jobs):
        for j in range(cur_index, len(jobs)):
            if jobs[j][0] > cur_time:
                cur_index = j
                break
            elif ask_time <= jobs[j][0] <= cur_time:  # 현재시점 전에 들어왔던 요청 heap에 추가
                heapq.heappush(h, (jobs[j][1], jobs[j][0]))
                if j == len(jobs)-1:
                    cur_index = len(jobs)
        if h:
            work_time, ask_time = heapq.heappop(h)
            ever += (cur_time-ask_time) + work_time
            cur_time += work_time
            i += 1
        else:
            cur_time += 1

    return ever//len(jobs)
