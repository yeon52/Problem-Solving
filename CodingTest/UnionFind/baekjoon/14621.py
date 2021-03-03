import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sex = ['0']*(N+1)
school = []
parent = [0]*(N+1)
sex[1:] = input().split()
result = 0
group = N
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(M):
    u,v,d = map(int, input().split())
    school.append((d,u,v))

school.sort()

for i in range(1,N+1):
    parent[i] = i

for i in school:
    d,u,v = i

    if find_parent(u)!=find_parent(v) and sex[u]!=sex[v]:
        union_parent(u,v)
        result += d
        group-=1

if group>1:
    print(-1)
else:
    print(result)

