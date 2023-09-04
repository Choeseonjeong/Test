# 글자 이어 붙여 문자열 만들기


def solution(my_string, index_list):
    return "".join(my_string[int(i)] for i in index_list)


# main
my_string = input()
index_list = list(input().split(","))

print(solution(my_string, index_list))
