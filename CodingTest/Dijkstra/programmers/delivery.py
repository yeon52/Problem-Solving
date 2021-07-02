#배달, 다익스트라
import heapq


def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)]*(N+1)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    dijkstra(graph, 1, distance)
    for i in distance[1:]:
        if i <= K:
            answer += 1

    return answer
