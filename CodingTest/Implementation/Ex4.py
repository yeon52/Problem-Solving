# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여
# 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한값을 이어서 출력한다.
# 예를 들어 K1A5CB7이 들어오면 ABCKK13을 출력한다.


S = input()
sum = 0
result = ''
for s in S:
    if s.isdigit():
        sum += int(s)
    else:
        result += s

result = sorted(result)
if sum != 0:
    result += str(sum)

print("".join(result))


# 다른풀이
# S = input()
# sum = 0
# i = 0
# while i < len(S):
#     if S[i].isdigit():
#         sum += S.count(S[i]) * int(S[i])
#         S = S.replace(S[i], "")
#     else:
#         i+=1
#
# S = sorted(S)
# if sum != 0:
#     S += str(sum)
# print("".join(S))
