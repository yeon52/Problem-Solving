def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}
    for genre in genres:
        dic[genre] = 0
        dic2[genre] = []

    for genre, play in zip(genres, plays):
        dic[genre] += play

    for i, (genre, play) in enumerate(zip(genres, plays)):
        dic2[genre].append((play, i))

    dic = sorted(dic.items(), reverse=True)
    dic2 = sorted(dic2.items(), key=lambda x: x[1][0], reverse=True)
    print(dic2)
    # for key in dic:

    return answer
