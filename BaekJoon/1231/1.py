#  카드 2
from collections import deque


def solution(n):
    queue = deque(range(1, n + 1))
    while len(queue) > 0:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]


print(solution(6))
