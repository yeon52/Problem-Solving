#입국심사, 이진탐색
# 시간으로 이분탐색을 하는게 포인트

def solution(n, times):
    times.sort()
    start = 1
    end = times[-1] * n

    while start <= end:
        poss_n = 0
        mid = (start + end) // 2

        for i in times:
            poss_n += mid//i

        if poss_n < n:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    return result
