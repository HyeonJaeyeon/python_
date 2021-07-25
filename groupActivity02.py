import re #정규표현식.. ^^..

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    answer = []
    hi = []

    for i in files:
        hi.append(re.split("(\d+)", i)) #정수기준으로 나눔

    a = sorted(hi, key = lambda x: (x[0].upper(), int(x[1]))) #처음 단어를 upper로 바꿔준 후 순서대로 sort 
    #같을 시에 정수로 변환한 x[1]기준으로 sort

    for i in a:
        answer.append("".join(i)) #""(구분자 없음) 합치기

    return answer

print(solution(files))