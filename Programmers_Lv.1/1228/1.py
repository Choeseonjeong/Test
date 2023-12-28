# 없는 숫자 더하기


def solution(numbers):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return sum([i for i in a if i not in numbers])


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
