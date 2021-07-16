N = int(input())

queue = list(map(int,input().split())) #queue: 현재 줄 서있는 곳 FIFO

stack = [] #stack: 한 명씩만 설 수 있는 공간 LIFO
num = 1 #num: 현재 받을 순서
while queue:
    if queue[0] == num: #현재 순서와 queue의 첫번째 사람의 번호가 같을 때
        queue.pop(0) #큐에서 pop 해줌
        num += 1 #순서 증가
    else:
        stack.append(queue.pop(0)) #순서 다르면 나가서 옆공간으로 가슈
    
    while stack:
        if stack[-1] == num: #스택에서 가장 위에 뭐가 있는지 알려면 stack[-1] 쓰면 됨
            #맨 위에 사람이랑 순서랑 같을 때
            stack.pop() #나가라
            num += 1 #순서 증가
        else: break #아님 말고

if not stack:
    print("Nice(^_^)")
else:
    print("Sad(T_T)")