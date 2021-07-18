board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):

    length = len(board)
    hi = []
    basket = []
    answer = 0
 

    for i in range(length):
        colu = []
        for j in range(length):
            colu.append(board[j][i])
        hi.append(colu)

    for k in moves:
        while hi[k-1][0] == 0: #맨 앞 0(즉, 인형이 없으면)   -->여기서 자꾸 오류가 남
            hi[k-1].pop(0) #0 안나올 때까지 삭제

    for l in moves:
        if (len(hi[l-1])) > 0: #hi에 인형이 하나 이상일 때
            basket.append(hi[l-1].pop(0)) #첫번째 인형을 빼자
            if (len(basket)) > 1: 
                if basket[-1] == basket[-2]: #바구니 두개값 같으면
                    basket.pop()
                    basket.pop()
                    answer += 2


            else: continue

    return answer




print(solution(board, moves))
