# 전화번호 목록, 해시

# 첫 풀이
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

# 해시사용
# def solution(phone_book):

#     dic = {}
#     for i in phone_book:
#         dic[i] = 1

#     for i in phone_book:
#         tmp = ''
#         for j in i:
#             tmp+=j
#             if tmp in dic and tmp!=i:
#                 return False
#     return True
