import math
from collections import deque


def solution(progresses, speeds):
    day_need = [
        math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))
    ]

    result = []
    queue = deque()

    for i in day_need:
        if not queue or queue[0] >= i:
            queue.append(i)
        else:
            result.append(len(queue))
            queue.clear()
            queue.append(i)
    result.append(len(queue))
    return result


print(solution([93, 30, 55], [1, 30, 5]))


# not queue : 큐가 비어있는지 확인
