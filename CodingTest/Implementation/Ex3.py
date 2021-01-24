# 시뮬레이션 & 완전탐색

# 행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표 평면이다.
# 왕실 정원의 특정한 한칸에 나이트가 서있다.
# 나이트는 L자 형태로만 이동할 수 있으며, 정원밖으로는 나갈 수 없다.
# 1. 수평으로 두칸 이동 후 수직으로 한칸 이동
# 2. 수직으로 두칸 이동 후 수평으로 한칸 이동
# 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를
# 출력하는 프로그램을 작성하시오.
# 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.

locate = input()

x, y = int(locate[1]), ord(locate[0])-96
# 갈 수 있는 8가지 방향
steps = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (-1,-2),(1,-2)]
cnt = 0

for step in steps:
    nx, ny = x, y
    nx += step[0]
    ny += step[1]
    if 0 < nx <= 8 and 0 < ny <= 8:
        cnt += 1

print(cnt)


### 처음 답 ###
# locate = input()
#
# x, y = int(locate[1]), ord(locate[0])-96
# # L, R, U, D
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# cnt = 0
#
# for i in range(4):
#     nx, ny = x, y
#     nx += 2 * dx[i]
#     ny += 2 * dy[i]
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     if i>1:
#         for j in range(2):
#             nx2, ny2 = nx, ny
#             nx2 += dx[j]
#             ny2 += dy[j]
#             if 0 < nx2 <= 8 and 0 < ny2 <= 8:
#                 cnt += 1
#     else:
#         for j in range(2,4):
#             nx2, ny2 = nx, ny
#             nx2 += dx[j]
#             ny2 += dy[j]
#             if 0 < nx2 <= 8 and 0 < ny2 <= 8:
#                 cnt+=1
# print(cnt)
