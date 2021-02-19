#크루스칼

import sys

def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

N = int(input())
dis = []
planet = []
parent = [0]*N
d = []
result = 0

for i in range(N):
    x,y,z = map(int, input().split())
    planet.append((x,y,z,i))

for i in range(N):
    parent[i] = i

planet.sort(key=lambda x:x[0])
for i in range(N-1):
    dis.append((abs(planet[i][0]-planet[i+1][0]),planet[i][3],planet[i+1][3]))

planet.sort(key=lambda x:x[1])
for i in range(N-1):
    dis.append((abs(planet[i][1]-planet[i+1][1]),planet[i][3],planet[i+1][3]))

planet.sort(key=lambda x:x[2])
for i in range(N-1):
    dis.append((abs(planet[i][2]-planet[i+1][2]),planet[i][3],planet[i+1][3]))

dis.sort()
for i in dis:
    c, a, b = i
    if find_parent(parent,a) != find_parent(parent,b): #사이클 확인
        union_parent(parent,a,b) #그룹화
        result += c #비용 기록

print(result)