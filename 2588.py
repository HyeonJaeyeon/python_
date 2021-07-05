a = int(input()) #정수형으로 변환
b = int(input()) #각 자리수 b,c,d에 대입
b1 = int(b//100)
b2 = int(b%100//10)
b3 = int(b%10)

ans1=int(a*b3)
ans2=int(a*b2)
ans3=int(a*b1)
ans4=(ans1+ans2*10+ans3*100) #10을 곱해줌으로써 한칸씩 밀려남

print(ans1)
print(ans2)
print(ans3)
print(ans4)

