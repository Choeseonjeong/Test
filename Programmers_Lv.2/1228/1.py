# 최댓값과 최솟값


def solution(s):
    s = s.split(" ")
    a = sorted(list(map(int, s)))
    return str(a[0]) + " " + str(a[-1])


print(solution("-1 -2 -3 -4"))
