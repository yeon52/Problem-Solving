#타겟넘버, dfs

from collections import deque
result = []


def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append(0)

    bfs(0, 0, numbers)
    answer = result.count(target)
    return answer


def bfs(cnt, number, numbers):
    if cnt == len(numbers):
        result.append(number)
        return
    bfs(cnt+1, number+numbers[cnt], numbers)
    bfs(cnt+1, number-numbers[cnt], numbers)
