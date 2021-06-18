# 로또의 최고순위와 최저순위 , 2021 Dev-Matching
def solution(lottos, win_nums):
    #     answer = []
    #     cnt_correct = 0
    #     zero = lottos.count(0)

    #     for i in lottos:
    #         if i!=0 and i in win_nums:
    #             cnt_correct+=1
    #             win_nums.remove(i)

    #     #최고
    #     if cnt_correct + zero >=2:
    #         answer.append(6-(cnt_correct+zero)+1)
    #     else:
    #         answer.append(6)

    #     #최저
    #     if cnt_correct>=2:
    #         answer.append(6-cnt_correct+1)
    #     else:
    #         answer.append(6)

    #     return answer

    # 개선
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]  # 맞힌 개수별 순위 저장
    cnt_correct = 0
    zero = lottos.count(0)

    for i in lottos:
        if i != 0 and i in win_nums:
            cnt_correct += 1

    answer.append(rank[cnt_correct + zero])
    answer.append(rank[cnt_correct])

    return answer
