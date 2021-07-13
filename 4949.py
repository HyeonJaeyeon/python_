def calc(sth):
    stack = []
    #sth = input() #입력
    stack.extend(sth) #각 문자를 스택에 넣음
    sum = [0,0] #각 sum을 0으로 정의

    for i in range(len(stack)):
        if stack[i] == "(":
            sum[0] +=1
        elif stack[i] == ")":
            sum[0] -=1
        elif stack[i] == "[":
            sum[1] +=1
        elif stack[i] == "]":
            sum[1] -=1

        if sum[0] < 0 or sum[1] < 0:
            return('NO')
            break

    if sum[0] > 0 or sum[1] > 0:
            return('NO')
    elif sum[0] == 0 and sum[1] == 0:
        return('YES')

while True:
    x = input()
    if x == ".":
        break
    
print(calc(x))