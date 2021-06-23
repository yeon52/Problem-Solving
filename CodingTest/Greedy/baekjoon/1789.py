S = int(input())
i = 0
sum = 0
cnt = 0
while True:
    i += 1
    sum += i
    if sum > S:
        print(i-1)
        break