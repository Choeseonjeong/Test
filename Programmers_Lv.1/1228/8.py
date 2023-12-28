# 문자열 내림차순으로 배치하기


def solution(n):
    return "".join(sorted(n, reverse=True))


print(solution("Zbcdefg"))
