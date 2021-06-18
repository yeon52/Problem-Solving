#체육복, 탐욕법

def solution(n, lost, reserve):
    answer = n-len(lost)
    rm = []
    
    for i in range(1,n+1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)
            answer +=1

    for i in reserve:
        if len(lost)==0:
            break
        if i-1 in lost:
            lost.remove(i-1)
            answer+=1
        elif i+1 in lost:
            lost.remove(i+1)
            answer+=1
        
        
    return answer