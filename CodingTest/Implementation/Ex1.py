# 시뮬레이션 - 상하좌우 이동
# 여행가 A는 NxN 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1x1크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1,1)이며,
# 가장 오른쪽 좌표는 (N,N)에 해당한다. 여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며,
# 시작 좌표는 항상 (1,1)이다.
#
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D중 하나의 문자가 반복적으로 적혀있다.
# L : 왼쪽으로 한칸 이동
# R : 오른쪽으로 한칸 이동
# U : 위로 한칸 이동
# D : 아래로 한칸 이동

N = int(input())
move = input().split()
nx, ny = 1, 1
# R, U, L, D
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in move:
    if i == 'R':
        if nx+dx[0]<1 or ny+dy[0]<1 or nx+dx[0]>N or ny+dy[0]>N:
            continue
        nx += dx[0]
        ny += dy[0]
    elif i == 'U':
        if nx+dx[1]<1 or ny+dy[1]<1 or nx+dx[0]>N or ny+dy[0]>N:
            continue
        nx += dx[1]
        ny += dy[1]
    elif i == 'L':
        if nx+dx[2]<1 or ny+dy[2]<1 or nx+dx[0]>N or ny+dy[0]>N:
            continue
        nx += dx[2]
        ny += dy[2]
    elif i == 'D':
        if nx+dx[3]<1 or ny+dy[3]<1 or nx+dx[0]>N or ny+dy[0]>N:
            continue
        nx += dx[3]
        ny += dy[3]

print(nx, ny)

# 다른 답
# n = input()
# x, y = 1, 1
# plans = input().split()
# 
# #L, U, R, D
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types = ['L','R','U','D']
# 
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
# 
#     if nx<1 or ny<1 or nx>n or ny>n:
#         continue
#     x,y = nx, ny
# 
# print(x,y)
