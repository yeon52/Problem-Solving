#뉴스 클러스터링, 2018 kakao blind recruitment

def solution(str1, str2):
    answer = 0
    str1_arr = []
    str2_arr = []
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            str1_arr.append(tmp.lower())
            
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if tmp.isalpha():
            str2_arr.append(tmp.lower())
    
    a = set(str1_arr)
    b = set(str2_arr)
    
    union = list(a|b)
    intersection = list(a&b)
    
    union_cnt = 0
    inter_cnt = 0
    
    for i in union:
        union_cnt += max(str1_arr.count(i),str2_arr.count(i))
    
    for i in intersection:
        inter_cnt += min(str1_arr.count(i),str2_arr.count(i))
    
    if union_cnt==0 and inter_cnt == 0:
        answer = 1
    else:
        answer = inter_cnt/union_cnt
        
    return int(answer*65536)