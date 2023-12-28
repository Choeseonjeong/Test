#  제일 작은 수 제거하기


def solution(n):
    a = sorted(n)[0]
    for i in n:
        if i == a:
            n.remove(i)
    return n if len(n) != 0 else [-1]


# min 쓰기
print(solution([10]))
