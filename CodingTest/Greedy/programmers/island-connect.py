# 섬 연결하기, 크루스칼 알고리즘(그리디)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


def solution(n, costs):
    answer = 0
    parent = [0]*n
    for i in range(n):
        parent[i] = i

    costs = sorted(costs, key=lambda x: x[2])
    print(costs)
    for cost in costs:
        a, b, d = cost
        print(find_parent(parent, a), find_parent(parent, b))
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += d

    return answer
