#순위, 그래프

def solution(n, results):
    answer = 0

    wins = [[] for _ in range(n + 1)]  # 나한테 이긴사람
    loses = [[] for _ in range(n + 1)]  # 나한테 진 사람

    for win, lose in results:
        wins[lose].append(win)
        loses[win].append(lose)

    for i in range(1, n + 1):
        for j in wins[i]:
            for k in loses[i]:
                if not j in wins[k]:
                    wins[k].append(j)

        for j in loses[i]:
            for k in wins[i]:
                if not j in loses[k]:
                    loses[k].append(j)

    for win, lose in zip(wins, loses):
        if len(win) + len(lose) == n - 1:
            answer += 1

    return answer
