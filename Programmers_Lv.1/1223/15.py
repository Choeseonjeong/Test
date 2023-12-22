# 콜라츠 추측


def solution(num):
    count = 0
    if num == 1:
        return 0
    while True:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
        if num == 1:
            break
        elif count >= 500:
            return -1
    return count


print(solution(626331))
