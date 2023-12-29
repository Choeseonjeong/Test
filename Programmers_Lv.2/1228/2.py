# JadenCase 문자열 만들기


def solution(s):
    a = s.split(" ")
    b = ""
    for i in range(len(a)):
        a[i] = a[i].capitalize()
    return " ".join(a)


print(solution("3people unFollowed me"))
