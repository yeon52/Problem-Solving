#위장, 해시
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = []

    for i in clothes:
        dic[i[1]].append(i[0])

    for i in dic:
        answer *= (len(dic[i])+1)

    return answer-1
