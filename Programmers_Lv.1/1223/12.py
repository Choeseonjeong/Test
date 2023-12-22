# 하샤드 수


def solution(x):
    a = sum(map(int, str(x)))
    return True if x % a == 0 else False


print(solution(12))
