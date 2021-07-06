def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        tmp = s[:i]
        cnt = 1
        split_s = ''
        for j in range(i, len(s)+1, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    split_s += tmp
                else:
                    split_s += str(cnt) + tmp
                    cnt = 1
            tmp = s[j:j+i]
        if len(s) % i > 0:
            split_s += s[-(len(s) % i):]
        answer = min(answer, len(split_s))
    return answer
