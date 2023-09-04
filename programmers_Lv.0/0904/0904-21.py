# 뒤에서 5등 위로


def solution(num_list):
    num_list.sort()
    return num_list[5:]


# main
num_list = input().split(",")
print(solution(num_list))
