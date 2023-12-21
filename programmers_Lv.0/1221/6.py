def solution(n, k):
    return int(n * 12000) + int((k - int(n / 10)) * 2000)


print(solution(10, 3))
