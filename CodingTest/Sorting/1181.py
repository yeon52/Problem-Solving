##조건이 있는 단어정렬, 시간제한 2초

### 직접 길이비교와 같은단어 없애기 넣어서 quicksort 구현
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail
            if len(x) < len(pivot) or (len(x) == len(pivot) and x < pivot)]
    right = [x for x in tail
             if len(x) > len(pivot) or (len(x) == len(pivot) and x > pivot)]
    return quick_sort(left) + [pivot] + quick_sort(right)

N = int(input())
words = []
for i in range(N):
    words.append(input())

words = quick_sort(words)

for i in range(len(words)):
    print(words[i])


# 함수사용 - nlogn

# N = int(input())
# words = []
# for i in range(N):
#     words.append(input())

# words = set(words)
# words = list(words)
# words.sort()
# words.sort(key=lambda x:len(x))
#
# for i in range(len(words)):
#     print(words[i])
