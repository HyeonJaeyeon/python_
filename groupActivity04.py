def solution(places):
    answer = []
    
    for seats in places:
        seat = []
        cnt = 0

        for seat in seats:
            seat.append(list(seat))
        
        for i in range(5):
            for j in range(5):
                if seat[i][j] == "P":
                    if i+1<5: 
                        if seat[i+1][j] == "P": #오른칸 사람 있으면
                            cnt +=1
                            break
                        if seat[i+1][j] == "O": #오른칸 비었는데
                            if i+2<5: #오른쪽 두번째칸 차있으면
                                if seat[i+2][j] == "P":
                                    cnt +=1
                                    break
                    if j+1<5:
                        if seat[i][j+1] == "P": #밑칸 사람 있으면
                            cnt +=1
                            break
                        if seat[i][j+1] == "O": #없는데
                            if j+2<5:
                                if seat[i][j+2] == "P": #그 밑에 있으면
                                    cnt +=1
                                    break
                    if i+1<5 and j+1<5: #대각선차례입니다. .. ... 개많네 공부를 열심히해서 다시는 이렇게 노가다로 안풀것이ㅏㄷ.. 정말이다..
                        if seat[i+1][j+1] == "P" and (seat[i+1][j] == "O" or seat[i][j+1] == "O"): #아무튼 그 뭐시기 거리때매 옆 밑 칸 다 파티션 있어야 함
                            cnt +=1
                            break
                    
                    if i+1<5 and j-1>=0: #이 부분은 생각을 하지 못했다 윗 대각선 ..
                        if seat[i+1][j-1] == "P" and (seat[i+1][j] == "O" or seat[i][j-1] == "O"):
                            cnt +=1
                            break
        if cnt > 0:
            answer.append(0)
        else:
            answer.append(1)

    return answer