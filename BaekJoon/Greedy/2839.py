#2839 - 그리디, 설탕배달

#5로 최대한 나눠야 최소값이 나옴
#5로 나눠지면 다 나누고 끝
#나눠지지 않으면 3을 하나씩 빼면서 나눠질때까지.

N = int(input())
bag = 0

while 1:
    if N % 5 == 0:
        bag += N // 5
        break
    else:
        if N < 3:
            bag = -1
            break
        else:
            N -= 3
            bag += 1
print(bag)
