#스도쿠, 백트래킹
#python3로는 시간초과 pypy3만 통과..

import sys
input = sys.stdin.readline

def chk_row(n,x):
    if n in m[x]:
        return False
    return True

def chk_col(n,y):
    for i in range(9):
        if m[i][y] == n:
            return False
    return True

def chk_mask(n,x,y):
    start_x, start_y = x // 3 * 3, y // 3 * 3

    for i in range(3):
        for j in range(3):
            if m[start_x + i][start_y + j] == n:
                return False
    return True

def sudoku(k):
    global chk
    if k==len(blank): #빈칸을 모두 채우면 츨력하고
        for i in range(9):
            for j in range(9):
                print(m[i][j],end=' ')
            print()
        sys.exit()

    x, y = blank[k]
    for n in range(1,10):
        if chk_row(n,x) and chk_col(n,y) and chk_mask(n,x,y):
            m[x][y] = n
            sudoku(k+1)
            m[x][y] = 0

m = []
blank = []
for i in range(9):
    m.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if m[i][j] == 0:
            blank.append((i,j))
global chk
chk = False
sudoku(0)