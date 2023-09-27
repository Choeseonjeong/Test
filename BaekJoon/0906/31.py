# 기능개발
import math
from collections import deque


def solution(progresses, speeds):
    a = []
    stack = []
    front = 0
    for i in range(len(progresses)):
        b = (100 - progresses[i]) / speeds[i]
        a.append(math.ceil(b))

    for i in range(len(a)):
        if a[i] > a[front]:
            stack.append(i - front)
            front = i
    stack.append(len(a) - front)

    return stack


# main
# print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# 5,10,1,1,20,1
# deque로 옆에가 더 크면 popleft
