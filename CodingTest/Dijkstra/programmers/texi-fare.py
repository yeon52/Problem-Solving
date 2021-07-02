# 합승택시요금, 최단경로 - 다익스트라 or 플로이드 워셜

# 다익스트라
import heapq

def dijkstra(graph, start):
    q = []
    distance = [int(1e9)]*len(graph)
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

    return distance


def solution(n, s, a, b, fares):
    answer = int(1e9)
    # 총 합 = 같이 가는 지점(k)까지의 거리 + k~a까지 거리 + k~b까지 거리 --> 최솟값
    graph = [[] for _ in range(n+1)]

    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))

    distanceS = dijkstra(graph, s)

    for k in range(n+1):
        distanceK = dijkstra(graph, k)
        answer = min(answer, distanceS[k]+distanceK[a]+distanceK[b])

    return answer

# 플로이드 워셜
# def solution(n, s, a, b, fares):
#     answer = int(1e9)
#     #총 합 = 같이 가는 지점(k)까지의 거리 + k~a까지 거리 + k~b까지 거리 --> 최솟값
#     graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==j:
#                 graph[i][j] = 0

#     for i, j, c in fares:
#         graph[i][j]=c
#         graph[j][i]=c

#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

#     for k in range(n+1):
#         answer = min(answer, graph[s][k]+graph[k][a]+graph[k][b])

#     return answer
