import sys
import math
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    if find_parent(a)<find_parent(b):
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
star = []
dis = []
parent = [0]*N
for i in range(N):
    x,y = map(float, input().split())
    star.append((x,y))
    parent[i] = i

for i in range(N):
    for j in range(i+1,N):
        x1,y1 = star[i]
        x2,y2 = star[j]
        dist = round(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)),2)
        dis.append((dist,i,j))

dis.sort()
result = 0
for i in dis:
    d,a,b = i
    if find_parent(a)!=find_parent(b):
        union_parent(a,b)
        result += d

print(result)