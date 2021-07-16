N = int(input())

euna = []
for i in range(N):
    num = map(int,input().split())
    test = list(map(int,input().split()))
    a = list(range(len(test)))
    a[num[1]] = 'last'

order = 0

while True:
    if test[0] == max(test):
        order +=1

        if a[0] == 'last':
            print(last)
            break
        else:
            test.pop(0)
            a.pop(0)

    else: 
        test.append(test.pop(0))
        a.append(a.pop(0))