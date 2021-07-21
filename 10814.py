import sys

N = int(sys.stdin.readline())

list = []

for i in range(N):
    [age,name] = sys.stdin.readline().split() # 나눠서 x, y에 넣어줌
    age = int(age)
    list.append([age,name])

print(list[0])

list.sort(key = lambda x : (x[0])) #람다 함수 -> 함수 정의 간단하게
# list를 list[0] 기준으로 먼저 정렬
# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬

for i in range(N):
    print(list[i][0], list[i][1])