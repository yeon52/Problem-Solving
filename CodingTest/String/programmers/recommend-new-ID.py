# 신규 아이디 추천, 문자열, 2021 kakao blind recruitment
def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i != '.' and i != '_' and i != '-' and not i.isdigit() and not i.isalpha():
            new_id = new_id.replace(i, '')

    # 3 #4
    new_id = new_id.split('.')
    while '' in new_id:
        new_id.remove('')
    new_id = '.'.join(new_id)

    # 5
    if not new_id:
        new_id = 'a'

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]

    new_id = new_id.strip('.')

    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
