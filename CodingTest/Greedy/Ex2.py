# 각 자리가 숫자로만 이루어진 문자열 S가 주여졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
# 'x' 혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램.
# +보다 x를 먼저 계산하는 일반적인 방식과는 달리,
# 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정.

S = input()
result = int(S[0])
for i in range(1, len(S)):
    if result > 1 and int(S[i]) > 1:
        result *= int(S[i])
    else:
        result += int(S[i])

print(result)