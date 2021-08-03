import sys  #dfs로 풀어보기
input = sys.stdin.readline
sys.setrecursionlimit(10**9) #재귀 깊이를 늘려주란다... 런타임 에러 뜸

n = int(input())
board = [[] for _ in range(n+1)] #받은 값들 표시할 board[]

for _ in range(n-1):
    x, y = map(int,input().split()) #값 받기
    board[x].append(y)#board에 받은 값들 표시(양방향)
    board[y].append(x)

parents = [0 for _ in range(n+1)]
parents[1] = 1 #1의 부모노드는 1

def dfs(board, start_node, parents):
    for i in board[start_node]: #start_node의 자식 노드들 돌리기
        if parents[i] == 0: #parent 등록 안돼있으면
            parents[i] = start_node 
            dfs(board, i, parents) #걔네의 자식노드까지 계속 같은 루틴 (dfs)
        

dfs(board, 1, parents)
for i in range(2,n+1):
    print(parents[i])