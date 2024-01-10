from collections import deque


def solution(s):
    queue = deque()
    for i in s:
        if not queue or i == "(":
            queue.append(i)
        elif i == ")":
            if queue and queue[-1] == "(":
                queue.pop()
            else:
                return False

    return not queue


print(solution(")()("))
