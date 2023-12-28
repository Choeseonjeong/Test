# 나머지가 1이 되는 수 찾기


def solution(n):
    a = [i for i in range(1, n) if n % i == 1]
    return a[0]


print(solution(10))
