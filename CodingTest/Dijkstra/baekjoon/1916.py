#최소비용 구하기
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
        for i in bus[n]:
            dis = c+i[1]
            if distance[i[0]] > dis:
                distance[i[0]] = dis
                heapq.heappush(h,(dis,i[0]))

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for i in range(M):
    a,b,c = map(int, input().split())
    bus[a].append((b,c))

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])
