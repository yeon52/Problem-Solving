#모의고사, 완전탐색
def solution(answers):
    answer = []
    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if A[i % 5] == answers[i]:
            score[0] += 1
        if B[i % 8] == answers[i]:
            score[1] += 1
        if C[i % 10] == answers[i]:
            score[2] += 1

    max_score = max(score)
    for i in range(3):
        if max_score == score[i]:
            answer.append(i+1)
    return answer
