# 정수 제곱근 판별


def solution(n):
    num = n**0.5
    return (num + 1) ** 2 if num == int(num) else -1


print(solution(3))
