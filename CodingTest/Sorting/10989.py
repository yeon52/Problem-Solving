### 시간제한3초, 메모리제한 8mb 정렬
# 계수정렬 사용
import sys
input = sys.stdin.readline  # input()보다 빠름
N = int(input())
cnt = [0]*10001

for i in range(N):
    cnt[int(input())] += 1  # 메모리제한이 있으므로 리스트를 최대한 줄이기 위해 하나만 사용.

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i)
