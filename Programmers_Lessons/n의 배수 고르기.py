def solution(n, numlist):
    a = []
    for i in numlist:
        if i % n == 0:
            a.append(i)
    return a


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
