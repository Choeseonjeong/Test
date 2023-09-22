# 다음 큰 숫자


def solution(n):
    k = bin(n)
    KC = k.count("1")
    a = []
    while True:
        n += 1
        h = bin(n)
        HC = h.count("1")
        if KC == HC:
            break

    return int(h, 2)


# bin(n).count('1')도 가능함


def solution(n):
    k = bin(n).count("1")
    a = []
    while True:
        n += 1
        h = bin(n).count("1")
        if k == h:
            break

    return n


# 2진수 변환 : bin(n)
# 10진수 변환 :  int(k, 2)
# 2진수로 변환하고, 1이 같은 것을 만들고, 10진수로 변환하고 최소값찾기
# main
print(solution(78))
