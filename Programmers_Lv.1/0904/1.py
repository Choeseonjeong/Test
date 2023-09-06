# 정수 내림차순으로 배치하기


def solution(n):
    a = []
    for i in str(n):
        a.append(i)
        a.reverse()
    return "".join(a)


# main
n = int(input())
print(solution(n))
