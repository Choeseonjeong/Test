# 최솟값 만들기


def solution(a, b):
    a.sort()
    b.sort(reverse=True)

    return sum(a[i] * b[i] for i in range(len(b)))


# main
a = [1, 4, 2]
b = [5, 4, 4]

print(solution(a, b))
