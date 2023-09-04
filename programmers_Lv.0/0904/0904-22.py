# 배열 만들기 1


def solution(n, k):
    return list(i for i in range(k, n + 1, k))


# main
n = int(input())
k = int(input())
print(solution(n, k))
