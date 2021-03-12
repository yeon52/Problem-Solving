import sys
input = sys.stdin.readline

N = int(input())
dot = []
for i in range(N):
    dot.append(tuple(map(int, input().split())))

dot.sort()  # 시작점 기준으로 오름차순 정렬
result = 0
pos = -1e9
for i in dot:
    start, end = i
    if pos <= start:  # 겹치는 공간이 없을 때
        result += end - start
        pos = end
    elif end > pos:  # 포함하지 않고, 겹치는 부분이 있을 때
        result += end - pos
        pos = end

print(result)
