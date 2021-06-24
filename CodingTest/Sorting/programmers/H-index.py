#H-index, 정렬

def solution(citations):
    answer = 0
    for i in range(max(citations)):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt >= i:
            answer = max(answer, i)
    return answer
