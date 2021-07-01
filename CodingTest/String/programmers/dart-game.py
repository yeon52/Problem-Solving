# 다트 게임, 문자열, 2018 kakao blind recruitment
def solution(dartResult):
    answer = 0
    score = []
    if '10' in dartResult:
        dartResult = dartResult.replace('10', 'X')

    for i in dartResult:
        if i.isdigit():
            score.append(int(i))
        elif i == 'X':
            score.append(10)
        elif i == 'D':
            score[-1] **= 2
        elif i == 'T':
            score[-1] **= 3
        elif i == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        elif i == '#':
            score[-1] *= (-1)

    print(score)
    return sum(score)
