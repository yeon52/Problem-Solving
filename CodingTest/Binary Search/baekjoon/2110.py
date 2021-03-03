import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = []

for _ in range(N):
    x.append(int(input()))

def isPossible(mid):
    cnt = C - 1
    wifi = x[0]
    for i in range(1,N):
        if x[i]-wifi >= mid:
            wifi = x[i]
            cnt -=1
            if cnt == 0:
                return True
    return False

x.sort()

left = 1 #최소거리
right = x[N-1] #최대거리

while left<=right:
    mid = (left+right)//2
    if isPossible(mid):
        left = mid+1
    else:
        right = mid-1

print(right)






