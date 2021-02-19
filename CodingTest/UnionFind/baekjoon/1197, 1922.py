#크루스칼
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
edges = []
parent = [0]*(V+1)
result = 0

for _ in range(E):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

for i in range(1,V+1):
    parent[i] = i

edges.sort()

for i in edges:
    c, a, b = i
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += c

print(result)
