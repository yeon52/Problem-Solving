# 완전탐색, 소수 찾기
from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    prime = []
    num = list(numbers)
    for i in range(1, len(num)+2):
        p = set(list(map(int, map(''.join, permutations(num, i)))))
        for j in p:
            if is_prime(j):
                prime.append(j)

    return len(set(prime))
