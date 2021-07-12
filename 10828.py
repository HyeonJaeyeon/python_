import sys

stack = []
#length=len(stack)

def push (X):
    stack.append(X) #append: 리스트의 마지막에 요소 혹은 리스트 전체 삽입
    #extend: 리스트에 리스트 요소들을 풀어 삽입

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop()) #pop: 리스트의 맨 마지막 요소 돌려주고 삭제

def size():
    print(len(stack)) #len: 문자열의 문자 개수 반환 or 리스트 요소의 총 개수

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[len(stack)-1])

N = int(input())

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        order[1]

    elif order[0] == 'pop':
        pop()

    elif order[0] == 'size':
        size()

    elif order[0] == 'empty':
        print(empty())

    elif order[0] == 'top':
        top()