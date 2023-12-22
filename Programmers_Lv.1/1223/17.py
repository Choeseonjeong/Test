# 나누어 떨어지는 숫자 배열


def solution(arr, divisor):
    a = [i for i in arr if i % divisor == 0]
    a.sort()
    if len(a) != 0:
        return a
    else:
        return [-1]


print(solution([5, 9, 7, 10], 5))
