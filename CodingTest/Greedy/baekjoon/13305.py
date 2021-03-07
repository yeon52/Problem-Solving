#주유소, 그리디
import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
cur_pos = 0
i = 0

while i < N:
    if i == N-1:
        for j in range(cur_pos, i):
            result += price[cur_pos] * road[j]
        break

    if price[i] < price[cur_pos]:
        for j in range(cur_pos, i):
            result += price[cur_pos] * road[j]
        cur_pos = i
    i += 1

print(result)
