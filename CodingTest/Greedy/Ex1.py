# (이코테 2021) <1이 될때까지>
# 어떠한 수 N이 1이 될때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수구하기

N, K = map(int, input().split(" "))
cnt = 0

while N > 1:
    if N % K == 0:
        N = N // K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)

# # 교재 답
# n, k = map(int, input().split(" "))
#
# result = 0
#
# while True:
#     # n이 k로 나누어 떨어지는 수가 될때까지 빼기
#     target = (n//k)*k
#     result += (n-target)
#     n = target
#     # n이 k보다 작을 때 반복문 탈출
#     if n < k:
#         break
#     # k로 나누기
#     result +=1
#     n //=k
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)
