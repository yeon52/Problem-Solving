

# 가장 큰수

# 사전식 배열을 reverse로 하되, [30,3]인 경우는 3,30이 되어야하므로 이런 경우의 수를 위해 숫자가 최대 1000까지라고 했으므로 *3을 해줌.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
