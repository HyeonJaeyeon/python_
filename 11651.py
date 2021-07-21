import sys #시간 오류 떠서 이걸로 받아줌 앞으로 웬만하면 다 이걸로

N = int(sys.stdin.readline())

list = []

for i in range(N):
    [x,y] = map(int,sys.stdin.readline().split()) # 나눠서 x, y에 넣어줌
    list.append([x,y])

#sort로 정렬.. 알아두기
#첨에 수고시럽게 배운 정렬 이것 저것 쓰다가 자꾸 시간 오류뜸 
list.sort(key = lambda x : (x[1]))

for i in range(N):
    print(list[i][0],list[i][1])