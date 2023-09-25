# 0922 3문제

# 피보나치 수


def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567


# main
print(solution(5))
