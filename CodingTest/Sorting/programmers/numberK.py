# 정렬, k번쨰 수
def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])

    return answer
