# 올바른 괄호


# 2진수 변환 : int("101010",2)


def solution(s):
    answer = []
    cnt = 0
    zeroCnt = 0

    while True:
        if s == "1":
            break

        zeroCnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]

        cnt += 1

    answer = [cnt, zeroCnt]
    return answer


print(solution("110010101001"))
