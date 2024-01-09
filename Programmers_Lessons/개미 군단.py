# 장군 : 5
# 병정 : 3


def solution(hp):
    return (hp // 5) + ((hp % 5) // 3) + (((hp % 5) % 3) // 1)


print(solution(24))
