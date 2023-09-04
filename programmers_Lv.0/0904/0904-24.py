# 특정한 문자를 대문자로 바꾸기


def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


# main
my_string = input()
alp = input()
print(solution(my_string, alp))
