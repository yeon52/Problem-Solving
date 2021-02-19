# 개미전사는 마을의 식량창고를 몰래 공격하려고 한다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며, 선택적으로 약탈하고자 한다.
# 이때 서로 인접한 식량창고를 약탈시 바로 알아챌 수 있다 .
# 따라서 들키지 않고 식량창고를 약탈하기 위해서는 최소 1칸이상 떨어진 식량창고들을 털어야한다.
# 이 때, 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하라


N = int(input())
food = list(map(int, input().split()))
d = [0]*N

#보텀업
d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+food[i])

print(d[N-1])