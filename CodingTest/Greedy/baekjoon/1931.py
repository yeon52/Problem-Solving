#1931 - 그리디, 회의실 배정
N = int(input())
conferences = []

for i in range(N):
    element = list(map(int, input().split(" ")))
    conferences.append(element)

conferences.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 오름차순 정렬(같을 경우 시작시간 오름차순 정렬)
cnt = 1

pre_confer = conferences[0]
for i in range(1, N):
    after_confer = conferences[i]
    if after_confer[0] >= pre_confer[1]:  # 다음 회의 시작 >= 현재 회의 끝
        cnt += 1
        pre_confer = after_confer

print(cnt)

