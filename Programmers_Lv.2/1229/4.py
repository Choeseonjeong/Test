# 숫자의 표현

# 연속한 자연수


def solution(n):
    a = []
    count = 0
    for i in range(1, n + 1):
        if sum(a) == n:
            count += 1
            a = []
        elif sum(a) > n:
            a = []
        else:
            a.append(i)
    return a, count


print(solution(15))
