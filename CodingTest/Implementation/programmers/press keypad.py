# 키패드 누르기, 2020 카카오 인턴십


def solution(numbers, hand):
    answer = ''
    #     cur_left = (3,0)
    #     cur_right = (3,2)

    #     for i in numbers:
    #         if i == 1 or i==4 or i==7 :
    #             answer+='L'
    #             cur_left = (i//3,0)
    #         elif i == 3 or i==6 or i==9:
    #             answer+='R'
    #             cur_right = (i//3-1,2)
    #         else:
    #             cur_Y = 1
    #             if i!=0 : cur_X = i//3
    #             else: cur_X = 3 #눌러야하는 키패드 위치

    #             dis_left = abs(cur_X-cur_left[0]) + abs(cur_Y-cur_left[1]) #왼손에서 거리
    #             dis_right = abs(cur_X-cur_right[0]) + abs(cur_Y-cur_right[1]) #오른손 거리

    #             if dis_left<dis_right:
    #                 answer+='L'
    #                 cur_left = (cur_X, cur_Y)
    #             elif dis_left>dis_right:
    #                 answer+='R'
    #                 cur_right = (cur_X, cur_Y)
    #             else:
    #                 if hand == 'left':
    #                     answer+='L'
    #                     cur_left = (cur_X, cur_Y)
    #                 else:
    #                     answer+='R'
    #                     cur_right = (cur_X, cur_Y)

    # 코드 개선
    l = {1: (0, 0), 2: (0, 1), 3: (0, 2),
         4: (1, 0), 5: (1, 1), 6: (1, 2),
         7: (2, 0), 8: (2, 1), 9: (2, 2),
         '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    cur_left = '*'
    cur_right = '#'

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            cur_left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            cur_right = i
        else:
            cur_key = l[i]
            lPos = l[cur_left]
            rPos = l[cur_right]
            dis_left = abs(cur_key[0] - lPos[0]) + \
                abs(cur_key[1] - lPos[1])  # 왼손에서 거리
            dis_right = abs(cur_key[0] - rPos[0]) + \
                abs(cur_key[1] - rPos[1])  # 오른손 거리
            if dis_left < dis_right:
                answer += 'L'
                cur_left = i
            elif dis_left > dis_right:
                answer += 'R'
                cur_right = i
            else:
                if hand == 'left':
                    answer += 'L'
                    cur_left = i
                else:
                    answer += 'R'
                    cur_right = i
    return answer
