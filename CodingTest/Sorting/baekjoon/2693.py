# N번째 큰수

T = int(input())
result = []
for i in range(T):
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    result.append(arr[2])

for i in result:
    print(i)
