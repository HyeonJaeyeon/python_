import sys
input=sys.stdin.readline

n, m, k= map(int, input().split())

board = [[0]*m for i in range(n)] #board: 받은 값들 다 표시
visited = [[0]*m for i in range(n)] #visited: 이따 방문한 애들 표시할 그룹

for i in range(k): #음식물 개수만큼 받아봥
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 #board 에 받은 값들 표시


def bfs(x,y):
    queue = []
    global cnt #global 변수로 선언해준다
    queue.append([x,y]) #queue에 넣고
    visited[x][y] = 1 #visited에 1을 넣어줌
    cnt+=1 #쓰레기 일단 하나 

    dx = [1,-1,0,0]#상하
    dy = [0,0,-1,1]#좌우

    while queue:
        x,y = queue.pop(0)
    
        for i in range(4): #1:상, 2:하, 3:좌, 4:우 ... 
            moveX, moveY = x + dx[i], y + dy[i]
            if 0<=moveX<n and 0<=moveY<m:
                if board[moveX][moveY] == 1 and visited[moveX][moveY] == 0 :
                    queue.append([moveX,moveY]) #queue에 움직인 값 넣어줌
                    visited[moveX][moveY] = 1 #visited에도 추가해주고
                    cnt += 1 #쓰레기 증가

cnt = 0 #쓰레기 개수
answer = 0 #총 쓰레기 개수

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            bfs(i,j)
            answer = max(answer, cnt) #max: 가장 큰 값을 반환
            cnt = 0 #쓰레기값 초기화

print(answer)