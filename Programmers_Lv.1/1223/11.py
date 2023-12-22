# 정수 내림차순으로 배치하기


def solution(n):
    n = list(map(int, str(n)))
    n.sort()
    n.reverse()
    return int("".join(map(str, n)))


print(solution(118372))
