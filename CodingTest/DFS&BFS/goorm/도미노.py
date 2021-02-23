a, b, c = map(int, input().split())
domino = [[] for _ in range(a+1)]

for i in range(b):
	d,e = map(int, input().split())
	domino[d].append(e)

hand = int(input())
cnt = 1

for i in range(hand, a+1):
	if domino[i]:
		cnt+=1

print(cnt)
