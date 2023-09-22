# 최솟값 만들기


def solution(a, b):
    a.sort()
    b.sort(reverse=True)
    return sum(a[i] * b[i] for i in range(len(a)))


# a의 최대값 찾고, b의 최솟값 찾고, 둘이 곱하고,더하고 각 리스트에서 삭제하고 무한반복
# main
a = [1, 4, 2]
b = [5, 4, 4]

print(solution(a, b))
