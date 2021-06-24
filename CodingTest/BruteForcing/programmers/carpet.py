#카펫, 완전탐색

import math


def solution(brown, yellow):

    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            height = i + 2
            width = yellow//i + 2
            if height*width == brown+yellow:
                answer = [width, height]

    return answer
