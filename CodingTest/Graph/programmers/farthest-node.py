# 가장 먼 노드, 그래프, bfs로 품

from collections import deque


def bfs(node, start, visited):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    result = [0]*(len(node))
    while q:
        n, cnt = q.popleft()
        for i in node[n]:
            if not visited[i]:
                q.append((i, cnt+1))
                result[i] = cnt+1
                visited[i] = True

    return result


def solution(n, edge):
    answer = 0
    node = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for s, e in edge:
        node[s].append(e)
        node[e].append(s)
    answer = bfs(node, 1, visited)

    return answer.count(max(answer))
