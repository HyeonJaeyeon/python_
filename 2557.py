a, b = map(int,input().split()) 
#입력값을 split(공백)으로 구분하여 a, b에 저장
#int로 변환하여 저장, map-> 반복처리
print(a+b)
print(a-b)
print(a*b)
print(a//b) #'/' 소수점 15자리까지 표현, '//' 정수부분만
print(a%b)