# 어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우,
# 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
# 하지만 x라는 도시에서 y라는 도시로 전보를 보내고자 한다면, x에서 y로 향하는 통로가 설치되어 있어야한다.
# x->y통로는 있지만 y->x 통로가 없다면 y는 x로 전보를 보내지 못한다.
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 c에서 보낸 메시지를 받게 되는
# 도시의 개수는 총 몇개이며 도시들이 모두 메시지를 받는데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

import heapq
INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for _ in range(M):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if dis > distance[now]:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(C)
cnt = 0
result = []
for i in distance:
    if i != INF:
        cnt+=1
        result.append(i)

print(cnt-1, end=" ")
print(max(result))