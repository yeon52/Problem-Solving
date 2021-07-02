# 메뉴 리뉴얼, 2021 kakao blind recruitment

# 조합 구현과 처음 되는대로 짠 코드,,
# def combinations(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations(arr[i + 1:], r - 1):
#                 yield [arr[i]] + next


# def solution(orders, course):
#     cnt_course = [{} for _ in range(len(course))]
#     result = []
#     comb = [[] for _ in range(len(course))]
#     for i in orders:
#         for index, c in enumerate(course):
#             for k in list(combinations(i, c)):
#                 k.sort()
#                 tmp = ''.join(k)
#                 if not tmp in comb[index]:
#                     comb[index].append(tmp)

#     for index, i in enumerate(comb):
#         for j in i:
#             for k in orders:
#                 cnt = 0
#                 for char in j:
#                     if char in k:
#                         cnt += 1
#                 if cnt == len(j):
#                     if j in cnt_course[index]:
#                         cnt_course[index][j] += 1
#                     else:
#                         cnt_course[index][j] = 1
#     tmp = []
#     for i in cnt_course:
#         if i:
#             tmp.append(max(i.values()))

#     for i, j in zip(tmp, cnt_course):
#         if i > 1:
#             for key in j:
#                 if j[key] == i:
#                     result.append(key)

#     result.sort()

#     return result



# 더 간결한 코드

from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = []
    comb = [[] for _ in range(len(course))]
        
    for c in course:
        temp = []
        for o in orders:
            temp += combinations(sorted(o), c)
        cnt_course = Counter(temp)
        if cnt_course:
            max_val = max(cnt_course.values())
            for key in cnt_course:
                if cnt_course[key] == max_val and max_val>1:
                    result.append(''.join(key))
    result.sort()
    return result
