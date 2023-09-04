# 조건에 맞게 수열 변환하기 1


def solution(arr):
    n = []
    for i in arr:
        if int(i) >= 50 and int(i) % 2 == 0:
            n.append(i / 2)
        elif int(i) < 50 and int(i) % 2 != 0:
            n.append(i * 2)
        else:
            n.append(i)
    return n


# main
arr = input().split(",")
print(solution(arr))
