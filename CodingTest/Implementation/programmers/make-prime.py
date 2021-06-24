# 소수만들기

import math
from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    arr = combinations(nums, 3)

    for i in arr:
        if is_prime(sum(i)):
            answer += 1

    return answer
