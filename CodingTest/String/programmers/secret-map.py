# 비밀지도, 비트연산, 2018 kakao blind recruitment

# 생각나는대로 짠 코드
# def solution(n, arr1, arr2):
#     answer = []
#     map1 = []
#     map2 = []
#     for i, j in zip(arr1, arr2):
#         tmp = format(i, 'b')
#         while len(tmp) < n:
#             tmp = '0'+tmp
#         map1.append(list(tmp))

#         tmp2 = format(j, 'b')
#         while len(tmp2) < n:
#             tmp2 = '0'+tmp2
#         map2.append(list(tmp2))

#     for i in range(n):
#         for j in range(n):
#             if map1[i][j] == '1' or map2[i][j] == '1':
#                 map1[i][j] = '#'
#             else:
#                 map1[i][j] = ' '

#     for i in map1:
#         answer.append(''.join(i))

#     return answer

# 비트연산을 이용한 풀이
def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        tmp = str(bin(i | j))[2:]
        tmp = tmp.rjust(n, '0')
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)

    return answer
