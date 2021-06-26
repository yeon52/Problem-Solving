# 베스트 앨범, 해쉬(딕셔너리)
def solution(genres, plays):
    answer = []
    dic = {}  # 합
    dic2 = {}
    for genre in genres:
        dic[genre] = 0
        dic2[genre] = []

    for genre, play in zip(genres, plays):
        dic[genre] += play
    for i, (genre, play) in enumerate(zip(genres, plays)):
        dic2[genre].append((play, i))

    for genre in genres:
        dic2[genre] = sorted(
            dic2[genre], key=lambda x: (x[0], -x[1]), reverse=True)
    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

    for key in dic:
        for play, i in dic2[key][:2]:
            answer.append(i)

    return answer
