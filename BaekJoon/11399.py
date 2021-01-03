#11399 - 그리디

# N = int(input())
# P = [int(i) for i in input().split(" ")]
# P_time = [0]*N
# P.sort() #시간의 합이 최소가 되려면 적게 걸리는 순으로 줄을 서야함.
# acc = 0
# for i in range(N):
#     acc += P[i]
#     P_time[i] = acc #누적합 저장
#
# print(sum(P_time))

N = int(input())
P = [int(i) for i in input().split(" ")]
P.sort()
result = 0
for i in range(N):
    result += sum(P[:i+1])
print(result)
