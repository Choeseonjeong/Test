# 문자열 내 p와 y의 개수
# 0921


def solution(s):
    Pcount = 0
    Ycount = 0
    for i in s:
        if i == "p" or i == "P":
            Pcount += 1
        elif i == "y" or i == "Y":
            Ycount += 1
    if Pcount == Ycount:
        return True
    else:
        return False

    # true, false 한 줄로 끝내는 방법


# return Pcount == Ycount   / 같으면 true, 다르면 false 반환


s = str("pPoooyY")
print(solution(s))
