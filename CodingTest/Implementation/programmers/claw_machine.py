# 크레인 인형뽑기, 카카오 2020 개발자 겨울인턴십

def solution(board, moves):
    answer = 0
    box = []

    for i in moves:
        for j in range(len(board)):
            doll = board[j][i-1]
            if doll == 0:
                continue
            else:
                board[j][i-1] = 0
                if len(box) != 0 and box[-1] == doll:
                    answer += 2
                    box.pop()
                    break
                else:
                    box.append(doll)
                    break
    print(box)
    return answer
