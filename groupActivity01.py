board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):

    length = len(board)
    hi = []
    basket = []
    answer = 0
 

    for i in range(length): #
        colu = [] #hi에 넣은 후 초기화
        for j in range(length):
            colu.append(board[j][i]) #각 열의 요소을 뽑아서
        hi.append(colu) #hi에 넣어줌 , hi: 열들의 모임

    for k in moves:
        while hi[k-1][0] == 0: #맨 앞 0(즉, 인형이 없으면)   -->밑에 for문이랑 합치면 여기서 자꾸 오류가 남
            hi[k-1].pop(0) #0 안나올 때까지 삭제

    for l in moves:
        if (len(hi[l-1])) > 0: #moves가 가리키는 줄의 인형이 하나 이상일 때
            basket.append(hi[l-1].pop(0)) #첫번째 인형을 빼자
            if (len(basket)) > 1: #바구니에 두개 이상일 때 (같은 값 두개를 빼야되므로 1 이하면 out of range 오류가 남)
                if basket[-1] == basket[-2]: #바구니 맨 위 두개값 같으면 
                    basket.pop() #위에서부터
                    basket.pop() #하나 더 !
                    answer += 2 

    return answer



print(solution(board, moves))
