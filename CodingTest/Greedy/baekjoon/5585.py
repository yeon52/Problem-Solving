price = int(input())

changes = 1000-price
coin = [500,100,50,10,5,1]
cnt = 0

for i in coin:
    if changes >= i:
        cnt += changes // i
        changes = changes%i

print(cnt)