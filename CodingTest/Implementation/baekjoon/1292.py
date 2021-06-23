A, B = map(int, input().split())
arr = []
cnt, i = 0, 1

while cnt < B:
    for j in range(i):
        arr.append(i)
        cnt += 1
    i += 1

print(sum(arr[A-1:B]))
