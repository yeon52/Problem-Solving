N = input()
arr = list(map(int, input().split()))
max = -1000001
min = 1000001

for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

print(str(min)+" "+str(max))
