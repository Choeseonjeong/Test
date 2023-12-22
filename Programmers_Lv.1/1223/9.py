# 자연수 뒤집어 배열로 만들기


def solution(n):
    a = list(map(int, str(n)))
    a.reverse()
    return a


print(solution(12345))
