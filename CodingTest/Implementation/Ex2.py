# 완전탐색
# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램.

N = int(input())  # 0<=N<24
cnt = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            word = str(h) + str(m) + str(s)
            if '3' in word:
                cnt += 1

print(cnt)