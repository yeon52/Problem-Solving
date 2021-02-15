# 미래도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
# 방문 판매원 A는 현재 1번 회사에 위치해 있으며, x번 회사에 방문해 물건을 판매하고자 한다.
# 미래도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일.
# 또한 연결된 2개의 회사는 양방향으로 이동할 수 있고, 정확히 1만큼의 시간으로 이동할 수 있다.
# 또한 A는 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 존재한다.
# A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아가서 함께 커피를 마실 예정이다.
# A가 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 최소시간을 계산하는 프로그램을 작성하시오

# 다익스트라 알고리즘
# import heapq
# INF = int(1e9)
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dis, now = heapq.heappop(q)
#         if dis > distance[now]:
#             continue
#         for i in graph[now]:
#             cost = dis + 1
#             if distance[i] > cost:
#                 distance[i] = cost
#                 heapq.heappush(q,(cost,i))
#
# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# distance = [INF]*(N+1)
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# X, K = map(int, input().split())
#
# dijkstra(1)
# k_len = distance[K]
# distance = [INF]*(N+1)
# dijkstra(K)
# X_len = distance[X]
# result = k_len+X_len
# if result >= INF:
#     print(-1)
# else:
#     print(result)

#플로이드 워셜 알고리즘

INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = graph[1][K]+graph[K][X]

if result >= INF:
    print(-1)
else:
    print(result)