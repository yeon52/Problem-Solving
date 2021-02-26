# n명의 병사가 무작위로 나열되어있다. 각 병사는 특정한 값의 전투력을 보유하고 있다.
# 병사를 배치할 떼는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용, 그러면서도 남아 있는
# 병사의 수가 최대가 되도록 하고 싶다.
# 병사에 대한 정보가 주어졌을 떄, 남아 있는 병사의 수가 최대가 되도록 하기 위해서
# 열외 시켜야 하는 병사의 수를 출력하는 프로그램

#가장 긴 증가하는 부분수열의 반대!
n = int(input())
power = list(map(int, input().split()))
d = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if power[i] < power[j]:
            d[i] = max(d[i],d[j]+1)

print(n-max(d))

#가장 긴 증가하는 부분수열
# n = int(input())
# power = list(map(int, input().split()))
# d = [1]*n
#
# for i in range(1,n):
#     for j in range(0,i):
#         if power[i] > power[j]:
#             d[i] = max(d[i],d[j]+1)
#
# print(max(d))