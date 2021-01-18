#1919 - 문자열, 애너그램
word1 = list(input())
word2 = list(input())
if len(word1) > len(word2):
    word1, word2 = word2, word1

cnt = 0
for i in word1:
    if i in word2:
        word2.remove(i)
        cnt += 1

print(len(word1) + len(word2) - cnt)
