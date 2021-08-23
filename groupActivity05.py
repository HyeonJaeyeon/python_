#우선순위 큐 이용, 그리디 알고리즘
from queue import PriorityQueue
import sys
input=sys.stdin.readline

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    answer = 0
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        previous = now
    
    target = k - sum_value + 1
    length = len(q.queue)
    temp = (target - 1) // length
    result = sorted(q.queue, key = lambda x:x[1])
    target -= temp * length

    answer = result[target - 1][1]
    
    return answer

print(solution([3, 1, 2], 5))