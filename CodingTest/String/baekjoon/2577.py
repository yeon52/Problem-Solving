#2577 - 문자열, 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)
for i in range(10):
    print(result.count(str(i)))

#2
# A = int(input())
# B = int(input())
# C = int(input())
#
# result = str(A * B * C)
# cnt_num = [0] * 10
#
# for i in result:
#     cnt_num[int(i)]=+1
#
# for i in range(10):
#     print(cnt_num[i])

#3
# A = int(input())
# B = int(input())
# C = int(input())
#
# result = A * B * C
# cnt_num = [0] * 10
#
# while (1):
#     if (result == 0):
#         break
#     for i in range(10):
#         if (result % 10 == i):
#             cnt_num[i] += 1
#             result = result // 10
#             break
#
# for i in range(10):
#     print(cnt_num[i])
