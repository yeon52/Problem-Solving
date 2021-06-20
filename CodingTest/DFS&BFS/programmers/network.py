#네트워크,  bfs
from collections import deque


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = []
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    for i in range(n):
        if bfs(i, graph, visited):
            answer += 1
    return answer


def bfs(v, graph, visited):
    if v in visited:
        return False
    queue = deque()
    queue.append(v)
    visited.append(v)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not i in visited:
                queue.append(i)
                visited.append(i)

    return True
