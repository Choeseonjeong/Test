# 부분 문자열


def solution(str1, str2):
    return 1 if str1 in str2 else 0


# main
str1 = input().split(",")
str2 = input().split(",")
print(solution(str1, str2))
