# N으로 표현
def solution(N, number):
    answer = -1
    dp = []
    n = str(N)
    if N == number:
        answer = 1
    else:
        for i in range(8):
            dp.append([int(n * (i+1))])

        for i in range(1, 8):
            for j in range(i):
                for q in dp[j]:
                    for k in dp[i-j-1]:
                        dp[i].append(q+k)
                        dp[i].append(q-k)
                        dp[i].append(q*k)
                        if k != 0:
                            dp[i].append(q//k)
            if number in dp[i]:
                answer = i+1
                break

    return answer
