import sys
input = sys.stdin.readline

K = int(input())
result = [[] for _ in range(K)] #만들어주야..

tree = list(map(int,input().split()))

def recurs(hi, first, last): #재귀함수
    if first == last:
        result[hi].append(tree[first])
        return
    middle = (first + last)//2
    result[hi].append(tree[middle])
    recurs(hi+1, first, middle-1)
    recurs(hi+1, middle + 1, last)

recurs(0,0,len(tree)-1)

for i in result:
    print(*i) #* unpacking

    


