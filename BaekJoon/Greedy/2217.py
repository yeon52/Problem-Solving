#2217 - 그리디, 문자열, 로프
# N = int(input())
# rope = []
#
# for i in range(N):
#     rope.append(int(input()))
#
# rope.sort()
# k = N
# max_weight = min(rope)*N
#
# while k > 1:
#     del rope[0]
#     min_rope = rope[0]
#     k = len(rope)
#     weight = k*min_rope
#     if weight > max_weight:
#         max_weight = weight
#
# print(max_weight)

N = int(input())
rope = []

for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
max_weight = rope[0]

for i in range(1, N):
    weight = rope[i] * (i + 1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)
