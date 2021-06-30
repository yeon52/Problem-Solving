#단어변환, bfs

from collections import deque


def chk_word(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [False]*len(words)
    while q:
        nw, cnt = q.popleft()
        if nw == target:
            answer = cnt
            break
        for i, word in enumerate(words):
            if chk_word(word, nw) and not visited[i]:
                q.append((word, cnt+1))
                visited[i] = True

    return answer
