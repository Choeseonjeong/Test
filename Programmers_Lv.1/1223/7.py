# 문자열 내 p와 y의 개수


def solution(n):
    n = n.lower()
    p = n.count("p")
    y = n.count("y")
    if p == y:
        return True
    else:
        return False


print(solution("Pyy"))
