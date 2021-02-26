#피보나치 함수
#DP
import sys
input = sys.stdin.readline

T = int(input())
result = []
use_input = []

for i in range(T):
    use_input.append(int(input()))
r = max(use_input)
d_0 = [0]*(r+1)
d_1 = [0]*(r+1)
d_0[0:2] = [1,0]
d_1[0:2] = [0,1]

for i in range(2, r+1):
    d_0[i] = d_0[i - 1] + d_0[i - 2]
    d_1[i] = d_1[i - 1] + d_1[i - 2]


for i in use_input:
    print(d_0[i],d_1[i])