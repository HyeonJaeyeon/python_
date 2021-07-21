#정렬 복습
N = int(input())
array = []

for i in range(N):
    array.append(int(input()))
"""#선택 정렬
for i in range(len(array)):
    min_index = i #일단 젤 첫값(작은값)저장
    for j in range(i+1, len(array)): #i+1부터 N미만
        if array[min_index] > array[j]: #저장한 값보다 지금 값 작으면
            min_index = j #j를 min에 넣음
    array[i], array[min_index] =  array[min_index], array[i] #스와프"""

"""#삽입 정렬
for i in range(len(array)):
    for j in range(i, 0 -1): #i부터 0까지 -1씩 훑자
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] #왼쪽 더 작으면 스왑
        else:
            break #왼쪽보다 크면 그냥 거기 있어라
"""

"""#퀵 정렬
def quick_sort(array, start, end):
    if start >= end: #원소가 1개일 때
        return
    pivot = start
    left= start +1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1 #left가 end보다 크고 pivot값보다 클 때까지 반복
        
        while(right > start and array[right]>=array[pivot]):
            right -= 1 #right가 start보다 크고 pivot값보다 작을 때 까지 반복

        if(left > right): #엇갈린 경우 => 피벗과 right값을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈 X => left값과 right에 해당하는 값 교체
            array[left], array[right] = array[right], array[left]
        #left 와 right는 그냥 순서를 의미한다 헷갈 x !!

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
"""
"""#간단한 퀵 정렬
def quick_sort(array):
    if len(array)<=1:
        return array
    
    pivot = array[0] #처음 원소 피봇
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] #피봇보다 작은 값만 왼쪽에 넣어줌
    right_side = [x for x in tail if x > pivot] #피봇보다 큰 값만 오른쪽에 넣어줌

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
"""

for i in range(len(array)):
    print(array[i])


