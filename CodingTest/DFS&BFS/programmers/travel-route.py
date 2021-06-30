#여행경로, dfs

def dfs(dic, start, path, n):
    if len(path) == n+1:
        return path
    for i, ticket in enumerate(dic[start]):
        tmp = path[:]
        tmp.append(ticket)
        dic[start].pop(i)

        res = dfs(dic, ticket, tmp, n)

        dic[start].insert(i, ticket)

        if res:
            return res


def solution(tickets):
    dic = {}
    visited = {}
    for s, e in tickets:
        if s not in dic:
            dic[s] = []
        if e not in dic:
            dic[e] = []
        dic[s].append(e)

    for key in dic:
        dic[key].sort()

    n = len(tickets)
    return dfs(dic, 'ICN', ['ICN'], n)


# 다른풀이
# from collections import deque
# result = []
# def dfs(dic, start):
#     for i in dic[start]:
#         dfs(dic,i)
#         result.append(i)

# def solution(tickets):
#     answer = []
#     dic = {}
#     visited={}
#     stack = ['ICN']
#     path = []
#     for s,e in tickets:
#         if s in dic:
#             dic[s].append(e)
#         else:
#             dic[s] = [e]

#     for key in dic:
#         dic[key].sort(reverse=True)

#     while stack:
#         s = stack[-1]
#         if not s in dic or len(dic[s])==0:
#             path.append(stack.pop())
#             continue
#         n = dic[s].pop()
#         stack.append(n)

#     return path[::-1]
