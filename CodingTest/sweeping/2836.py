import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dot = []
for i in range(N):
    dot.append(tuple(map(int, input().split())))

dot = sorted(dot, key=lambda x: x[1])
pos = 0  # 현재위치
result = 0

for i in dot:
    start, end = i
    if end < start:  # 반대로 가는 경우에만 스위핑 해주면 됨.
        end, start = start, end
        if pos <= start:  # 겹치는 공간이 없을 때
            result += end-start
            pos = end
        elif end > pos:  # 포함하지 않고, 겹치는 부분이 있을 때
            result += end - pos
            pos = end

result = result*2 + M  # 왔다가야하기 때문에 x2

print(result)
