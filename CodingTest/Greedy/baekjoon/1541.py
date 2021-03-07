#잃어버린 괄호
import sys
input = sys.stdin.readline
ex = input().rstrip()
li = []
num = 0
for i in ex:
    if i=='+' or i=='-':
        li.append(num)
        li.append(i)
        num=0
    else:
        num = num*10+int(i)

li.append(num)
sum_li = []
sum = li[0]
#빼기가 나오면 묶기시작, 다음 빼기가 나오면 괄호 닫기
for i in range(1,len(li)):
    if li[i]=='-':
        sum_li.append(sum)
        sum=0
    elif li[i]!='+':
        sum+=li[i]
sum_li.append(sum)
result = sum_li[0]
for i in range(1,len(sum_li)):
    result = result - sum_li[i]

print(result)