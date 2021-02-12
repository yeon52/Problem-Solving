# N가지 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다
# 각 종류의 화폐는 몇개라도 사용할 수 있다. M원을 만들기 위한 최소한의 화폐개수를 출력하는 프로그램을 작성하라

import sys
sys.setrecursionlimit(10**6)

def coin_cnt(coin):
    if coin == 0:
        return 0

    if d[coin] != -1:
        return d[coin]

    d[coin] = 10001

    for i in m:
        if coin >= i:
            d[coin] = min(d[coin],coin_cnt(coin - i)+1)

    return d[coin]

n, k = map(int, input().split())
m = []
d = [-1]*10001

for i in range(n):
    m.append(int(input()))

result = coin_cnt(k)
if result == 10001:
    print(-1)
else:
    print(result)