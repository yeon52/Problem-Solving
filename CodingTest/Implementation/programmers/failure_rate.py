# 실패율, 2019 kakao blind recruitment
def solution(N, stages):
    answer = []
    rates = {}
    challenge = len(stages)
    for i in range(1, N+1):
        fail = stages.count(i)
        if challenge == 0 and fail == 0:
            rates[i] = 0
        else:
            rates[i] = fail/challenge
        challenge -= fail

    rates = sorted(rates.items(), key=lambda x: (x[1], -x[0]), reverse=True)

    for i, rate in rates:
        answer.append(i)

    return answer
