# 음양 더하기


def solution(absolutes, signs):
    a = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            a.append(absolutes[i])
        else:
            a.append(-absolutes[i])
    return sum(a)


print(solution([4, 7, 12], [True, False, True]))
