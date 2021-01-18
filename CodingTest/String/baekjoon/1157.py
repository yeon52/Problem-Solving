#1157 - 문자열, 단어공부
word = input()
word = word.upper()
words = []
cnt_word = []

for i in word:
    if i in words:
        cnt_word[words.index(i)] += 1
    else:
        words.append(i)
        cnt_word.append(1)

if cnt_word.count(max(cnt_word)) > 1:
    print("?")
else:
    index = cnt_word.index(max(cnt_word))
    print(words[index])

#2
# string = input()
# string = string.upper()
# words = set(string)
# max_cnt = 0
#
# for i in words:
#     if string.count(i) > max_cnt:
#         max_cnt = string.count(i)
#         result = i
#     elif string.count(i) == max_cnt:
#         result = '?'
#
# print(result)
