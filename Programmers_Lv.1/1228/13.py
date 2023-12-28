# 최대공약수와 최소공배수


# 최소공배수
def minSolution(n, m):
    for i in range(max(m, n), (m * n) + 1):
        if i % n == 0 and i % m == 0:
            return i


# 최대공약수
def MaxSolution(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i


def solution(n, m):
    return [MaxSolution(n, m), minSolution(n, m)]


print(solution(3, 12))
