#한수
import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(1,N+1):
    li = list(map(int, str(i)))
    if len(li) == 1:
        result+=1
        continue
    sub = li[1]-li[0]
    chk = 0
    for j in range(1, len(li)-1):
        if li[j+1] - li[j] != sub:
            chk = 1
            break
    if chk == 0:
        result +=1

print(result)