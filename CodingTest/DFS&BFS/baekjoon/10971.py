# 외판원 순회, dfs풀이

def dfs(graph, start, cost, visited, depth):
    global result, N
    if cost < result:
        if depth == N and graph[start][0] != 0:
            result = min(result, cost+graph[start][0])
            return
        visited[start] = True
        for i, ncost in enumerate(graph[start]):
            if ncost != 0 and not visited[i]:
                dfs(graph, i, cost + ncost, visited, depth+1)
                visited[i] = False


N = int(input())
W = []

result = 1000001*N
for i in range(N):
    W.append(list(map(int, input().split())))

visited = [False] * N
dfs(W, 0, 0, visited, 1)

print(result)
