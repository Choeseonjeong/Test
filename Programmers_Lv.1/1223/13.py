# 두 정수 사이의 합


def solution(a, b):
    if a < b:
        return sum([i for i in range(a, b + 1)])
    else:
        return sum([i for i in range(b, a + 1)])


print(solution(5, 3))
