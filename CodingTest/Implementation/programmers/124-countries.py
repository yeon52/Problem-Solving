# 124 나라의 숫자

def solution(n):
    q = []
    ans = ''
    dic = {1: 1, 2: 2, 0: 4}
    while n > 0:
        tmp = n % 3
        q.append(dic[tmp])
        n = n//3
        if tmp == 0:
            n -= 1

    while q:
        ans += str(q.pop())

    return ans

# 다른사람 풀이
# def change124(n):
#     num = ['1','2','4']
#     answer = ""


#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3

#     return answer
