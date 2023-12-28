# 내적


def solution(a, b):
    for i in range(len(a)):
        return sum(a[i] * b[i] for i in range(len(a)))


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
