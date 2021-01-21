# 한 마을에 모험가가 N명이 있다. 모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데,
# 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어짐.
# 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 최대 몇개의 모험가 그룹을 만들 수 있는지, N명의 모험가에 대한 정보가 주어졌을 때
# 여행을 떠날 수 있는 그룹 수의 최댓값 구하기

N = int(input())
adventurer = list(map(int, input().split(" ")))
adventurer.sort()
result = 0  # 그룹 수
i = 0
cnt = 0  # 그룹 내 인원 수
for i in range(N):
    cnt += 1
    if adventurer[i] <= cnt:
        cnt = 0
        result += 1
print(result)
