x = int(input())

d = [0]*(x+1)

for i in range(2,x+1):
    tmp = [d[i - 1] + 1]

    if i%3 == 0:
        tmp.append(d[i//3] +1)  #3으로 나눔

    if i%2 == 0:
        tmp.append(d[i//2] + 1) #2로나눔

    d[i] = min(tmp)

print(d[x])