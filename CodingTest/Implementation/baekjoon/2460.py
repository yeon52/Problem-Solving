train = []
cnt = 0
maxCnt = 0
for i in range(10):
    train.append(list(map(int, input().split())))

for Out, In in train:
    cnt -= Out
    cnt += In
    if cnt>maxCnt:
        maxCnt = cnt

print(maxCnt)