T = int(input())

#for i in range(T):
def calc():
    stack = []
    sth = input()
    stack.extend(sth) #extend는 요소 하나씩 낱개로 저장
    sum = 0

    for i in range(len(stack)):

        if stack[i] == "(":
            sum +=1
        elif stack[i] == ")":
            sum -=1
        if sum < 0:
            return('NO')
            break
    if sum > 0:
        return('NO')
    elif sum ==0:
        return('YES')
        
for i in range(T):
    print(calc())