# 이진수
from collections import deque

T = int(input())
binary = deque()

for i in range(T):
    n = int(input())
    while n != 0:
        binary.append(n % 2)
        n = n//2

    for i in range(len(binary)):
        if binary.popleft() == 1:
            print(i, end=' ')
    print()
