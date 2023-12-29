# 올바른 괄호


# 2진수 변환 : int("101010",2)


def solution(s):
    count = 0
    count_zero = 0
    while len(list(s)) == 1:
        count += 1
        s = "1"
    return count


print(solution("110010101001"))
