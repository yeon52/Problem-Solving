#사탕게임, 브루트포스, 구현

N = int(input())
candy = []
result = 0


def chkCandy(arr):  # 최대 사탕 개수
    max_cnt = 0
    cnt = 0
    for i in arr:  # 행 체크
        max_cnt = max(max_cnt, cnt)
        cnt = 1
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1

    for i in range(len(arr[0])):  # 열체크
        temp = []
        for j in range(len(arr[0])):
            temp.append(arr[j][i])
        max_cnt = max(max_cnt, cnt)
        cnt = 1
        for j in range(len(arr[0])-1):
            if temp[j] == temp[j + 1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1

    return max_cnt


for i in range(N):
    candy.append(list(input()))

for i in range(N):
    for j in range(N):
        if j+1 < N:
            a = candy[i][j]
            b = candy[i][j+1]
            if a != b:
                candy[i][j], candy[i][j+1] = b, a  # 바꿈
                result = max(chkCandy(candy), result)
                candy[i][j], candy[i][j + 1] = a, b  # 돌려놓기
        if i+1 < N:
            a = candy[i][j]
            b = candy[i+1][j]
            if a != b:
                candy[i][j], candy[i+1][j] = b, a  # 바꿈
                result = max(chkCandy(candy), result)
                candy[i][j], candy[i+1][j] = a, b  # 돌려놓기

if result == 0:
    result = chkCandy(candy)

print(result)
