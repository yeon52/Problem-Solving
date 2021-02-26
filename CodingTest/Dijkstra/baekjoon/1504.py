import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0
    while h:
        c,n = heapq.heappop(h)
        for i in graph[n]:
            dis = c+i[1]
            if distance[i[0]] > dis:
                distance[i[0]] = dis
                heapq.heappush(h,(dis,i[0]))

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())
tmp=tmp2 = 0

distance = [INF] * (N + 1)
dijkstra(1)
tmp += distance[v1]
distance = [INF] * (N + 1)
dijkstra(v1)
tmp += distance[v2]
distance = [INF] * (N + 1)
dijkstra(v2)
tmp += distance[N]

distance = [INF] * (N + 1)
dijkstra(1)
tmp2 += distance[v2]
distance = [INF] * (N + 1)
dijkstra(v2)
tmp2 += distance[v1]
distance = [INF] * (N + 1)
dijkstra(v1)
tmp2 += distance[N]

result = min(tmp,tmp2)

if result>=INF:
    print(-1)
else:
    print(result)
