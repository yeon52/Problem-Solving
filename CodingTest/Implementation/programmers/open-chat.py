# 오픈 채팅방, 2019 kakao blind recruitment
def solution(record):
    li = []
    answer = []
    dic = {}
    for i in record:
        state, uid = i.split()[:2]
        name = i.split()[-1]
        if state == 'Enter':
            dic[uid] = name
            li.append((uid, state))
        elif state == 'Leave':
            li.append((uid, state))
        elif state == 'Change':
            dic[uid] = name

    for i, s in li:
        pre = dic[i]+'님이 '
        if s == 'Enter':
            answer.append(pre+'들어왔습니다.')
        else:
            answer.append(pre+'나갔습니다.')

    return answer
