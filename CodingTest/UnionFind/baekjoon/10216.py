# Count Circle Groups
# 유니온파인드
import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def is_friend(a, b):
    x1,y1,r1 = a
    x2,y2,r2 = b
    if (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) <= (r1+r2)*(r1+r2): #접하거나 겹침
        return True
    return False

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    parent = [0]*N
    p = []
    ans.append(N)
    for i in range(N):
        x, y, r = map(int, input().split())
        p.append((x,y,r))
        parent[i] = i

    for i in range(N):
        for j in range(i+1,N):
            if is_friend(p[i],p[j]) and find_parent(i) != find_parent(j):
                union_parent(i,j)
                ans[-1] -= 1

for i in ans:
    print(i)