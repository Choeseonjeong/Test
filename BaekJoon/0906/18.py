# JadenCase 문자열 만들기


def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return " ".join(s)


# capitalize == 첫번재가 알파벳이면 대문자로, 나머지는 소문자로


# main
s = "3people unFollowed me"
print(solution(s))
