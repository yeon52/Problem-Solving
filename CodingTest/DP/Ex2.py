# 정수 x가 주어졌을 떄, 정수 x에 사용할 수 있는 연산은 다음과 같이 4가지.
# 1. x가 5으로 나누어 떨어지면 5로 나눈다.
# 2. x가 3으로 나누어 떨어지면 3로 나눈다.
# 3. x가 2 나누어 떨어지면 2로 나눈다.
# 5. x에서 1을 뺀다.
# x가 주어졌을 때 연산4개를 적절히 사용해서 값을 1로 만들고자 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하라

#보텀업
x = int(input())

d = [0]*30001

for i in range(2,x+1):
    tmp = [d[i - 1] + 1]

    if i%5 == 0:
        tmp.append(d[i//5] + 1)  #5로나눔

    if i%3 == 0:
        tmp.append(d[i//3] +1)  #3으로 나눔

    if i%2 == 0:
        tmp.append(d[i//2] + 1) #2로나눔

    d[i] = min(tmp)

print(d[x])
